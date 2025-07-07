1. [Web Security Academy](/web-security)  
2. [Essential skills](/web-security/essential-skills)  
  
# Essential skills  
  
We design the labs for the Web Security Academy to be as realistic as possible, but you should keep in mind that each lab demonstrates just one possible variation of a given vulnerability. In practice, it's important to be able to recognize subtly different occurrences of the same underlying bugs and know how to adapt the techniques you've learned accordingly.   
In this section, you'll learn some broadly applicable skills that will help you to apply what you've learned from our labs to other live targets. We cover a range of general tips and tricks, as well as how to use some of Burp's lesser-known features to optimize your workflow. We've also provided some additional labs, so you can test these out for yourself.   
We plan to expand this section to cover more essential skills in the near future.   
  
## Obfuscating attacks using encodings  
  
Simply copying the attacks from our lab solutions and attempting them on real sites will only get you so far. Websites that you test will have often already been audited by other users and had a number of patches applied to them. To take your skills further, you'll need to adapt the techniques you've learned to overcome these additional obstacles, unearthing vulnerabilities that other testers may have overlooked.   
In this section, we'll provide some suggestions on how you can obfuscate harmful payloads to evade input filters and other flawed defenses. Specifically, you'll learn how to use standard encodings to take advantage of misconfigurations and handling discrepancies between connected systems.   
  
#### Learn more

1. [Obfuscating attacks using encodings](/web-security/essential-skills/obfuscating-attacks-using-encodings)
2. [LAB SQL injection with filter bypass via XML encoding](/web-security/sql-injection/lab-sql-injection-with-filter-bypass-via-xml-encoding)  
  
## Using Burp Scanner during manual testing  
  
Testing for certain types of vulnerability can be fairly tedious, especially ones that involve trying numerous injection techniques in every controllable input. Doing this manually is often impractical due to real-life time constraints, which can lead to you missing critical vulnerabilities.   
There are a number of ways you can optimize your workflow by using Burp Scanner to supplement your own knowledge and intuition. Not only does this reduce the chance of you overlooking things, it can save you valuable time by helping you to rapidly identify potential attack vectors. This means you can concentrate your time and effort on things that can't be easily automated, such as working out how to exploit the vulnerable behavior or chain it with your other findings.   
  
#### Learn more

1. [LABS Using Burp Scanner during manual testing](/web-security/essential-skills/using-burp-scanner-during-manual-testing)  
  
## Identifying unknown vulnerabilities  
  
When attempting one of our labs, you usually know the exact vulnerability you need to look for. This is obviously not the case when testing genuine websites. To help you bridge this gap, we've created a mystery lab feature that lets you practice identifying vulnerabilities without any prior knowledge of them.   
  
#### Learn more

1. [LABS Mystery lab challenge](/web-security/mystery-lab-challenge)
