1. [Web Security Academy](/web-security)  
2. [HTTP Host header attacks](/web-security/host-header)  
  
# HTTP Host header attacks  
  
In this section, we'll discuss how misconfigurations and flawed business logic can expose websites to a variety of attacks via the HTTP Host header. We'll outline the high-level methodology for identifying websites that are vulnerable to HTTP Host header attacks and demonstrate how you can exploit this for the following kinds of attacks:   
  
1. [Password reset poisoning](/web-security/host-header/exploiting/password-reset-poisoning) LABS
2. [Web cache poisoning](/web-security/host-header/exploiting#web-cache-poisoning-via-the-host-header) LABS
3. [Exploiting classic server-side vulnerabilities](/web-security/host-header/exploiting#exploiting-classic-server-side-vulnerabilities)
4. [Bypassing authentication](/web-security/host-header/exploiting#accessing-restricted-functionality) LABS
5. [Virtual host brute-forcing](/web-security/host-header/exploiting#accessing-internal-websites-with-virtual-host-brute-forcing)
6. [Routing-based SSRF](/web-security/host-header/exploiting#routing-based-ssrf) LABS
7. [Connection state attacks](/web-security/host-header/exploiting#connection-state-attacks) LABS
![Host header attack](host-header-attacks.jpg)  
  
#### Labs  
  
If you're already familiar with the basic concepts behind HTTP Host header vulnerabilities and just want to practice exploiting them on some realistic, deliberately vulnerable targets, you can access all of the labs in this topic from the link below.   
  
1. [View all HTTP Host header labs](/web-security/all-labs#http-host-header-attacks)  
  
## What is the HTTP Host header?  
  
The HTTP Host header is a mandatory request header as of HTTP/1.1. It specifies the domain name that the client wants to access. For example, when a user visits `https://portswigger.net/web-security`, their browser will compose a request containing a Host header as follows:   
`GET /web-security HTTP/1.1 Host: portswigger.net`  
In some cases, such as when the request has been forwarded by an intermediary system, the Host value may be altered before it reaches the intended back-end component. We will discuss this scenario in more detail below.   
  
## What is the purpose of the HTTP Host header?  
  
The purpose of the HTTP Host header is to help identify which back-end component the client wants to communicate with. If requests didn't contain Host headers, or if the Host header was malformed in some way, this could lead to issues when routing incoming requests to the intended application.   
Historically, this ambiguity didn't exist because each IP address would only host content for a single domain. Nowadays, largely due to the ever-growing trend for cloud-based solutions and outsourcing much of the related architecture, it is common for multiple websites and applications to be accessible at the same IP address. This approach has also increased in popularity partly as a result of IPv4 address exhaustion.   
When multiple applications are accessible via the same IP address, this is most commonly a result of one of the following scenarios.   
  
### Virtual hosting  
  
One possible scenario is when a single web server hosts multiple websites or applications. This could be multiple websites with a single owner, but it is also possible for websites with different owners to be hosted on a single, shared platform. This is less common than it used to be, but still occurs with some cloud-based SaaS solutions.   
In either case, although each of these distinct websites will have a different domain name, they all share a common IP address with the server. Websites hosted in this way on a single server are known as "virtual hosts".   
To a normal user accessing the website, a virtual host is often indistinguishable from a website being hosted on its own dedicated server.   
  
### Routing traffic via an intermediary  
  
Another common scenario is when websites are hosted on distinct back-end servers, but all traffic between the client and servers is routed through an intermediary system. This could be a simple load balancer or a reverse proxy server of some kind. This setup is especially prevalent in cases where clients access the website via a content delivery network (CDN).   
In this case, even though the websites are hosted on separate back-end servers, all of their domain names resolve to a single IP address of the intermediary component. This presents some of the same challenges as virtual hosting because the reverse proxy or load balancer needs to know the appropriate back-end to which it should route each request.   
  
### How does the HTTP Host header solve this problem?  
  
In both of these scenarios, the Host header is relied on to specify the intended recipient. A common analogy is the process of sending a letter to somebody who lives in an apartment building. The entire building has the same street address, but behind this street address there are many different apartments that each need to receive the correct mail somehow. One solution to this problem is simply to include the apartment number or the recipient's name in the address. In the case of HTTP messages, the Host header serves a similar purpose.   
When a browser sends the request, the target URL will resolve to the IP address of a particular server. When this server receives the request, it refers to the Host header to determine the intended back-end and forwards the request accordingly.   
  
## What is an HTTP Host header attack?  
  
HTTP Host header attacks exploit vulnerable websites that handle the value of the Host header in an unsafe way. If the server implicitly trusts the Host header, and fails to validate or escape it properly, an attacker may be able to use this input to inject harmful payloads that manipulate server-side behavior. Attacks that involve injecting a payload directly into the Host header are often known as "Host header injection" attacks.   
Off-the-shelf web applications typically don't know what domain they are deployed on unless it is manually specified in a configuration file during setup. When they need to know the current domain, for example, to generate an absolute URL included in an email, they may resort to retrieving the domain from the Host header:   
`<a href="https://_SERVER['HOST']/support">Contact support</a>`  
The header value may also be used in a variety of interactions between different systems of the website's infrastructure.   
As the Host header is in fact user controllable, this practice can lead to a number of issues. If the input is not properly escaped or validated, the Host header is a potential vector for exploiting a range of other vulnerabilities, most notably:   
  
1. Web cache poisoning 
2. Business logic flaws in specific functionality 
3. Routing-based SSRF 
4. Classic server-side vulnerabilities, such as SQL injection 

## How do HTTP Host header vulnerabilities arise?  
  
HTTP Host header vulnerabilities typically arise due to the flawed assumption that the header is not user controllable. This creates implicit trust in the Host header and results in inadequate validation or escaping of its value, even though an attacker can easily modify this using tools like Burp Proxy.   
Even if the Host header itself is handled more securely, depending on the configuration of the servers that deal with incoming requests, the Host can potentially be overridden by injecting other headers. Sometimes website owners are unaware that these headers are supported by default and, as a result, they may not be treated with the same level of scrutiny.   
In fact, many of these vulnerabilities arise not because of insecure coding but because of insecure configuration of one or more components in the related infrastructure. These configuration issues can occur because websites integrate third-party technologies into their architecture without necessarily understanding the configuration options and their security implications.   
  
## Exploiting HTTP Host header vulnerabilities  
  
By now, you should have a good understanding of what the HTTP Host header is. For pentesters and bug bounty hunters, we've created some additional guidance on how you can identify and exploit these kinds of vulnerabilities for yourself. We've also provided some deliberately vulnerable LABS so that you can practice some of these techniques.   
  
#### Read more

1. [How to identify and exploit HTTP Host header vulnerabilities](/web-security/host-header/exploiting)  
  
## How to prevent HTTP Host header attacks  
  
To prevent HTTP Host header attacks, the simplest approach is to avoid using the Host header altogether in server-side code. Double-check whether each URL really needs to be absolute. You will often find that you can just use a relative URL instead. This simple change can help you prevent web cache poisoning vulnerabilities in particular.   
Other ways to prevent HTTP Host header attacks include:   
  
##### Protect absolute URLs  
  
When you have to use absolute URLs, you should require the current domain to be manually specified in a configuration file and refer to this value instead of the Host header. This approach would eliminate the threat of password reset poisoning, for example.   
  
##### Validate the Host header  
  
If you must use the Host header, make sure you validate it properly. This should involve checking it against a whitelist of permitted domains and rejecting or redirecting any requests for unrecognized hosts. You should consult the documentation of your framework for guidance on how to do this. For example, the Django framework provides the `ALLOWED_HOSTS` option in the settings file. This approach will reduce your exposure to Host header injection attacks.   
  
##### Don't support Host override headers  
  
It is also important to check that you do not support additional headers that may be used to construct these attacks, in particular `X-Forwarded-Host`. Remember that these may be supported by default.   
  
##### Whitelist permitted domains  
  
To prevent routing-based attacks on internal infrastructure, you should configure your load balancer or any reverse proxies to forward requests only to a whitelist of permitted domains.   
  
##### Be careful with internal-only virtual hosts  
  
When using virtual hosting, you should avoid hosting internal-only websites and applications on the same server as public-facing content. Otherwise, attackers may be able to access internal domains via Host header manipulation. 
