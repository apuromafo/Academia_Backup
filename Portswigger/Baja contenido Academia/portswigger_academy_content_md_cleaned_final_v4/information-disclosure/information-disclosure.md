1. [Web Security Academy](/web-security)  
2. [Information disclosure](/web-security/information-disclosure)  
  
# Information disclosure vulnerabilities  
  
In this section, we'll explain the basics of information disclosure vulnerabilities and describe how you can find and exploit them. We'll also offer some guidance on how you can prevent information disclosure vulnerabilities in your own websites.   
![Information disclosure infographic](information-disclosure.jpg)  
Learning to find and exploit information disclosure is a vital skill for any tester. You are likely to encounter it on a regular basis and, once you know how to exploit it effectively, it can help you to improve your testing efficiency and enable you to find additional, high-severity bugs.   
  
#### Labs  
  
If you're already familiar with the basic concepts behind information disclosure vulnerabilities and just want to practice exploiting them on some realistic, deliberately vulnerable targets, you can access all of the labs in this topic from the link below.   
  
1. [View all information disclosure labs](/web-security/all-labs#information-disclosure)  
  
## What is information disclosure?  
  
Information disclosure, also known as information leakage, is when a website unintentionally reveals sensitive information to its users. Depending on the context, websites may leak all kinds of information to a potential attacker, including:   
  
1. Data about other users, such as usernames or financial information 
2. Sensitive commercial or business data 
3. Technical details about the website and its infrastructure   
The dangers of leaking sensitive user or business data are fairly obvious, but disclosing technical information can sometimes be just as serious. Although some of this information will be of limited use, it can potentially be a starting point for exposing an additional attack surface, which may contain other interesting vulnerabilities. The knowledge that you are able to gather could even provide the missing piece of the puzzle when trying to construct complex, high-severity attacks.   
Occasionally, sensitive information might be carelessly leaked to users who are simply browsing the website in a normal fashion. More commonly, however, an attacker needs to elicit the information disclosure by interacting with the website in unexpected or malicious ways. They will then carefully study the website's responses to try and identify interesting behavior.   
  
### Examples of information disclosure  
  
Some basic examples of information disclosure are as follows:   
  
1. Revealing the names of hidden directories, their structure, and their contents via a `robots.txt` file or directory listing 
2. Providing access to source code files via temporary backups 
3. Explicitly mentioning database table or column names in error messages 
4. Unnecessarily exposing highly sensitive information, such as credit card details 
5. Hard-coding API keys, IP addresses, database credentials, and so on in the source code 
6. Hinting at the existence or absence of resources, usernames, and so on via subtle differences in application behavior   
In this topic, you will learn how to find and exploit some of these examples and more.   
  
#### Read more

1. [How to find and exploit information disclosure vulnerabilities](/web-security/information-disclosure/exploiting)  
  
## How do information disclosure vulnerabilities arise?  
  
Information disclosure vulnerabilities can arise in countless different ways, but these can broadly be categorized as follows:   
  
1. **Failure to remove internal content from public content**. For example, developer comments in markup are sometimes visible to users in the production environment. 
2. **Insecure configuration of the website and related technologies**. For example, failing to disable debugging and diagnostic features can sometimes provide attackers with useful tools to help them obtain sensitive information. Default configurations can also leave websites vulnerable, for example, by displaying overly verbose error messages. 
3. **Flawed design and behavior of the application**. For example, if a website returns distinct responses when different error states occur, this can also allow attackers to [enumerate sensitive data](/web-security/authentication/password-based#username-enumeration), such as valid user credentials. 

## What is the impact of information disclosure vulnerabilities?  
  
Information disclosure vulnerabilities can have both a direct and indirect impact depending on the purpose of the website and, therefore, what information an attacker is able to obtain. In some cases, the act of disclosing sensitive information alone can have a high impact on the affected parties. For example, an online shop leaking its customers' credit card details is likely to have severe consequences.   
On the other hand, leaking technical information, such as the directory structure or which third-party frameworks are being used, may have little to no direct impact. However, in the wrong hands, this could be the key information required to construct any number of other exploits. The severity in this case depends on what the attacker is able to do with this information.   
  
### How to assess the severity of information disclosure vulnerabilities  
  
Although the ultimate impact can potentially be very severe, it is only in specific circumstances that information disclosure is a high-severity issue on its own. During testing, the disclosure of technical information in particular is often only of interest if you are able to demonstrate how an attacker could do something harmful with it.   
For example, the knowledge that a website is using a particular framework version is of limited use if that version is fully patched. However, this information becomes significant when the website is using an old version that contains a known vulnerability. In this case, performing a devastating attack could be as simple as applying a publicly documented exploit.   
It is important to exercise common sense when you find that potentially sensitive information is being leaked. It is likely that minor technical details can be discovered in numerous ways on many of the websites you test. Therefore, your main focus should be on the impact and exploitability of the leaked information, not just the presence of information disclosure as a standalone issue. The obvious exception to this is when the leaked information is so sensitive that it warrants attention in its own right.   
  
## Exploiting information disclosure  
  
We've put together some more practical advice to help you identify and exploit these kinds of vulnerabilities. You can also practice these techniques using our interactive labs.   
  
#### Read more

1. [How to find and exploit information disclosure vulnerabilities](/web-security/information-disclosure/exploiting)  
  
## How to prevent information disclosure vulnerabilities  
  
Preventing information disclosure completely is tricky due to the huge variety of ways in which it can occur. However, there are some general best practices that you can follow to minimize the risk of these kinds of vulnerability creeping into your own websites.   
  
1. Make sure that everyone involved in producing the website is fully aware of what information is considered sensitive. Sometimes seemingly harmless information can be much more useful to an attacker than people realize. Highlighting these dangers can help make sure that sensitive information is handled more securely in general by your organization. 
2. Audit any code for potential information disclosure as part of your QA or build processes. It should be relatively easy to automate some of the associated tasks, such as stripping developer comments. 
3. Use generic error messages as much as possible. Don't provide attackers with clues about application behavior unnecessarily. 
4. Double-check that any debugging or diagnostic features are disabled in the production environment. 
5. Make sure you fully understand the configuration settings, and security implications, of any third-party technology that you implement. Take the time to investigate and disable any features and settings that you don't actually need. 
