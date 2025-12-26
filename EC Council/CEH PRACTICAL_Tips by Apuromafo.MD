 

# 🛡️   CEH Practical Exam

## 🔗 Recursos y Enlaces de Interés

  lista completa de referencias para el estudio del examen:

### Artículos y Writeups (Experiencias Reales)

* **Ome Murillo (2022):** [Examen CEH Practical 2022](https://medium.com/@ome.murillo/examen-ceh-practical-2022-a82ae0fb48c0)
* **AnonTuttuVenus:** [CEH Practical Exam Review](https://anontuttuvenus.medium.com/ceh-practical-exam-review-185ea4cef82a)
* **Lightkun Yagami:** [Passed EC-Council's CEH Practical](https://lightkun-yagami.medium.com/passed-ec-councils-certified-ethical-hacker-practical-20634b6f0f2)
* **Veeppiaar:** [EC-Council CEH v10 Practical Review](https://veeppiaar.medium.com/ec-council-ceh-v10-practical-exam-review-1b6c75dafbe6)

### Guías Técnicas y Wikis

* **The GuruSec:** [Certified Ethical Hacker Practical Wiki](https://book.thegurusec.com/certifications/certified-ethical-hacker-practical)
* **CyberSecurityUP (GitHub):** [Guide CEH Practical Master](https://github.com/CyberSecurityUP/Guide-CEH-Practical-Master)
* **Runmodule:** [Essential Tools for CEH Practical](https://runmodule.com/2020/12/13/tools-for-ceh-practical/)

### Video Tutorial

* **YouTube:** [¿Como rendir el CEH Practical y no morir en el intento?](https://www.youtube.com/watch?v=pjlV-n43sns)
 
---

## ❓ Banco de Preguntas (Escenarios Prácticos)

1. Realizar escaneo de vulnerabilidades para el servidor web `movies.cehorg.com` usando **OpenVAS** e identificar el nivel de severidad de la vulnerabilidad RPC.
2. Escaneo de vulnerabilidades para el host Linux en la red `172.16.0.0/24` usando **OpenVAS** y encontrar el número de vulnerabilidades de nivel "Medium".
3. Reconocimiento para CEHORG: encontrar la ubicación física del servidor web `www.certifiedhacker.com`. Nota: Formato Latitud, Longitud.
4. Identificar si `www.certifiedhacker.com` permite transferencia de zona DNS (**AXFR**). (Yes/No).
5. Identificar el número de máquinas vivas en la subred `172.16.0.0/24`.
6. Identificar la versión de **OpenSSH** en una máquina vulnerable en la red `192.168.0.0/24`.
7. Determinar el OS de la máquina que aloja una base de datos **MySQL** susceptible a Blind SQL Injection.
8. Encontrar la dirección IP del **Domain Controller** (DC).
9. Realizar host discovery e identificar el nombre **NetBIOS** del host en `10.10.10.25`.
10. Encontrar la IP de la máquina que tiene el puerto **21 (FTP)** abierto en la red `172.16.0.0/24`.
11. Realizar un escaneo intenso en `10.10.10.25` y encontrar el **FQDN** de la máquina.
12. ¿Cuál es el nombre de equipo DNS del Domain Controller?
13. Realizar enumeración **LDAP** e identificar cuántas cuentas de usuario están asociadas al dominio.
14. Realizar búsqueda LDAP en el DC y encontrar la versión del protocolo LDAP.
15. Identificar la IP de la máquina con el servicio **NFS** habilitado en la red `192.168.0.0/24`.
16. Realizar enumeración DNS en `www.certifiedhacker.com` y encontrar los nameservers (NS).
17. Encontrar la IP de la máquina con servicio **SMTP** en la red `192.168.0.0/24`.
18. Realizar enumeración **SMB** en `192.168.0.51` y verificar si el "Message signing" está habilitado (Yes/No).
19. Escaneo de vulnerabilidades con OpenVAS en el DC e identificar el número de vulnerabilidades "Medium".
20. Investigar el **CVE-2022-30171**: encontrar el "base score" y el impacto.
21. Crackear hashes **NTLM** almacenados en la carpeta Documents. ¿Cuál es el password del usuario **James**?
22. Crackear hashes NTLM en Documents. ¿Cuál es el password del usuario **Jones**?
23. **Escalada de Privilegios:** Tienes acceso de usuario en `172.16.0.11`. Escala a root y lee `rootflag.txt`. (Password: `LinuxPass`).
24. **Esteganografía:** Investigar el archivo `Confidential.txt` en `C:\Users\Admin\Documents` y extraer el mensaje oculto.
25. Investigar la imagen `vacation.bmp` en la máquina Windows y encontrar información oculta.
26. **Análisis de Malware:** Analizar `face.exe`. Encontrar el "File pos" para el texto `KERNEL32.dll` (excluir ceros).
27. Determinar la arquitectura de CPU (malware module) para el archivo ELF `Sample-ELF`.
28. Auditar contraseñas: encontrar el password del usuario **Adam** (Creds: `Administrator / CSCPa$$`).
29. Usar **Yersinia** para un ataque de **DHCP starvation**. Encontrar el Transaction ID de los paquetes DHCP Discover.
30. Analizar `sniffsession.pcap` e identificar qué protocolo se usó para realizar el sniffing.
31. Analizar `webtraffic.pcapng` y encontrar el ID del paquete que usa protocolo **ICMP**.
32. Analizar `CustomUDP.pcapng` y encontrar el tamaño de datos del paquete UDP en bytes.
33. Analizar `DoS.pcapng` y encontrar la dirección IP del atacante.
34. Conectarse a una máquina infectada con **spyware** y encontrar el flag oculto en la carpeta Documents.
35. **Covert Channels:** El archivo `Capture.pcapng` tiene un mensaje oculto en el campo **IP ID**. Analizar la sesión y extraer el mensaje.
36. Análisis dinámico: analizar un snapshot del registro del sistema y determinar si los "driver packages" cambiaron (Yes/No).
37. Monitoreo de servicios: encontrar el tipo de servicio asociado al nombre "afunix".
38. Analizar `movies.pcapng` y encontrar credenciales filtradas en texto plano.
39. Analizar `DDoS.pcapng` y determinar cuántas máquinas se usaron para iniciar el ataque.
40. Realizar **HTTP-recon** en `www.certifiedhacker.com` y encontrar la versión de **Nginx**.
41. Crackear credenciales FTP, obtener `flag.txt` y determinar su contenido.
42. Reconocimiento web en `movies.cehorg.com`: identificar el servidor HTTP utilizado.
43. Ataque de **SQL Injection** en `movies.cehorg.com` (Creds: `Jason / welcome`). ¿Cuántos usuarios hay en la DB?
44. Identificar el servicio de **Load Balancing** usado por `eccouncil.org`.
45. Identificar el **CMS** (Content Management System) usado por `www.cehorg.com`.
46. Ataque de fuerza bruta en `www.cehorg.com` para encontrar el password del usuario **Adam**.
47. **Parameter Tampering** en `movies.cehorg.com`: encontrar el usuario correspondiente al ID `1003`.
48. Explotar vulnerabilidad en puerto `8080` de un servidor Linux. Obtener contenido de `RootFlag.txt`.
49. Realizar test de **Clickjacking** en `www.certifiedhacker.com`. (¿Es vulnerable? Yes/No).
50. **Command Injection** en `10.10.10.25`: ¿Cuántas cuentas de usuario existen? (Excluir admin/guest).
51. Crackear hash MD5 del archivo `Hash.txt` subido vía **DVWA**.
52. **Banner Grabbing** en `movies.cehorg.com` para encontrar el **ETag**.
53. **Web Crawling** en `movies.cehorg.com`: identificar cuántos archivos `.png` hay en la carpeta `images`.
54. Test de **XSS** en `www.cehorg.com`. (¿Es vulnerable? Yes/No).
55. Analizar `sniffsession.pcap` para identificar el protocolo de sniffing utilizado.
56. Decodificar `EncodedFile.txt` (Password: `Pa$$w0rd`) para encontrar una dirección IP.
57. Descifrar `AccessCode.docx.aes` usando **Advanced Encryption Package** (Password: `qwerty`).
58. Descifrar volumen **VeraCrypt** llamado `secret` (Password: `test`) y contar los archivos dentro.
59. Integridad de archivos: comparar hashes MD5 en `FileHashes.txt` e identificar qué archivo fue alterado.
60. Analizar `IOT Traffic.pcapng` y encontrar el **Topic** del mensaje enviado al sensor.
61. Acceder a un móvil Android remotamente y borrar el archivo con información de cuenta. ¿Cuál era el valor numérico?
62. Analizar `Andro.pcapng` (Expert Info) para identificar la severidad de un ataque DoS desde el móvil.
63. Usar **PhoneSploit** para obtener una captura de pantalla del ataque **LOIC** e identificar IP objetivo y método de envío.
64. Auditoría de APK: analizar `AntiMalwarescanner.apk` y ver si pide permiso `Read-call-logs`.
65. Obtener el `KEYCODE-75` de un dispositivo móvil usando PhoneSploit.
66. Analizar `IOT Traffic.pcapng` (repetida, verificar topic del mensaje).
67. Analizar `NetworkNS_Traffic.pcapng` y encontrar el mensaje de alerta enviado al sensor.
68. Usar **Shodan.io** para identificar si la IP `166.150.247.183` pertenece a sistemas SCADA/ICS en US.
69. Usar **CrypTool** para descifrar `cryt-128-06encr.hex`. Identificar algoritmo y texto oculto.
70. Usar **Metasploit (wp_scanner)** para encontrar el password del usuario `john` en WordPress.
71. Encontrar un backdoor en Windows Server 2019 y leer el contenido del archivo secreto.
72. ¿Qué máquina de la red tiene el servicio **RDP (3389)** corriendo?
73. Acceder vía RDP a Server 2019 y recuperar un archivo del escritorio.
74. Usar **SNOW** para extraer contenido de un archivo con esteganografía.
75. Identificar IP de ataque DoS usando el archivo PCAP provisto.
76. Identificar IPs de un ataque **DDoS** y contar el total de máquinas atacantes.
77. Usar `dsss.py` para encontrar un link vulnerable a SQLi y obtener el número de teléfono de "Ketty".
78. Identificar qué método HTTP es vulnerable usando **OWASP ZAP**.
79. Descifrar archivo `des-ecb` para encontrar password e IP de un servidor FTP (User: `James`).
80. Encontrar el texto plano de un hash usando `hashes.com`.
81. Enumeración de usuarios en DC: ¿Qué cuenta existe además de john, sam y administrator?
82. Usar **BC Text Encoder** para decodificar un archivo.
83. Usar **Hydra** para atacar FTP y descargar `flag1.txt`.
84. Usar CrypTool para descifrar un número de cuenta (RC4, key length 14).
85. ¿Qué máquina tiene Blind SQLi y MySQL corriendo?
86. Explotar credenciales débiles de FTP en `192.168.0.0/24` y obtener `Credential.txt`.
87. Explotar `www.cehorg.com` y obtener el flag de la página con `page_id=84`.
88. Crackear credenciales SMB del usuario **Henry**, obtener `sniff.txt` y decodificar el secreto usando su password.
89. Recuperar `sa_code.txt` de una máquina remota usando un **RAT** ya instalado.
90. Explotar `training.cehorg.com` (`192.168.0.4`) y leer `Flag.txt`.
91. Encontrar el **Entry Point** (Address) del ejecutable `die-another-day`.
92. Explotar app de ejecución de comandos en Linux para leer `NetworkPass.txt`.
93. Acceder a un móvil, obtener un archivo `.elf` en la carpeta `scan` y calcular los últimos 4 dígitos del **SHA384** del archivo con mayor entropía.
94. Escaneo de vulnerabilidades en `172.20.0.16`: ¿Cuál es el puntaje de severidad de la vulnerabilidad "End of Life" del lenguaje web?
95. SQL Injection en `cybersec.cehorg.com` (`172.20.0.22`): obtener valor de la columna `Flag`.
96. Crackear Wi-Fi: analizar `WirelessCapture.cap` con `aircrack-ng` para encontrar la contraseña.
97. **Escalada Vertical:** Usar credenciales `smith / L1nux123` en Ubuntu, escalar a root y leer `imroot.txt`.

---

### 📝 Notas Finales para el Estudiante:

* **Gestión del Tiempo:** Tienes 6 horas para 20 preguntas. No te atasques en una con 14 aproximadamente ya pasas.

* **Google es tu amigo:** Si no recuerdas el parámetro de un comando (ej. `nmap -sV`), puedes buscarlo , además puedes armar una guia de apuntes para ese mismo día y evitar estar consultando comandos.

* **Parrot OS:** Casi todas las herramientas mencionadas (`Hydra`, `Sqlmap`, `Wireshark`, `Aircrack-ng`) vienen preinstaladas.
 


CEH Practical Sample Questions 
 
1.	Perform vulnerability scanning for the webserver hosting movies.cehorg.com using OpenVAS and identify the severity level of RPC vulnerability. 
2.	Perform vulnerability scanning for the Linux host in the 172.16.0.0/24 network using OpenVAS and find the number of vulnerabilities with severity level as medium. 
3.	You are performing reconnaissance for CEHORG and has been assigned a task to find out the physical location of one of their webservers hosting www.certifiedhacker.com. What are the GEO Coordinates of the webserver? Note: Provide answer as Latitude, Longitude. 
4.	Identify if the website www.certifiedhacker.com allows DNS zone transfer. (Yes/No) 
5.	Identify the number of live machines in 172.16.0.0/24 subnet. 
6.	While performing a security assessment against the CEHORG network, you came to know that one machine in the network is running OpenSSH and is vulnerable. Identify the version of the OpenSSH running on the machine. Note: Target network 192.168.0.0/24. 
7.	During a security assessment, it was found that a server was hosting a 
website that was susceptible to blind SQL injection attacks. Further investigation revealed that the underlying database management system of the site was MySQL. Determine the machine OS that hosted the database. 
8.	Find the IP address of the Domain Controller machine. 
9.	Perform a host discovery scanning and identify the NetBIOS name of the host at 10.10.10.25. 
10.	Find the IP address of the machine which has port 21 open. Note: Target network 172.16.0.0/24 
11.	Perform an intense scan on 10.10.10.25 and find out the FQDN of the machine in the network. 
12.	What is the DNS Computer Name of the Domain Controller? 
13.	Perform LDAP enumeration on the target network and find out how many user accounts are associated with the domain. 
14.	Perform an LDAP Search on the Domain Controller machine and find out the version of the LDAP protocol. 
15.	What is the IP address of the machine that has NFS service enabled? Note: Target network 192.168.0.0/24. 
16.	Perform a DNS enumeration on www.certifiedhacker.com and find out the name servers used by the domain. 
17.	Find the IP address of the machine running SMTP service on the 192.168.0.0/24 network. 
18.	Perform an SMB Enumeration on 192.168.0.51 and check whether the Message signing feature is enabled or disabled. Give your response as Yes/No. 
19.	Perform vulnerability scanning for the domain controller using OpenVAS and identify the number of vulnerabilities with severity level as "medium". 20. Perform a vulnerability research on CVE-2022-30171 and find out the base score and impact of the vulnerability 
21.	You are assigned a task to crack the NTLM password hashes captured by the internal security team. The password hash has been stored in the Documents folder of the Parrot Security console machine. What is the password of user James? 
22.	You are assigned a task to crack the NTLM password hashes captured by the internal security team. The password hash has been stored in the Documents folder of the Parrot Security console machine. What is the password of user Jones? 
23.	You have got user-level access to the machine with IP 172.16.0.11. Your task is to escalate the privileges to that of the root user on the machine and read the content in the rootflag.txt file. (Note: all the flag files are located at the root, Desktop, Documents, or Downloads folder for the respective users/machines). Note: use LinuxPass when asked for machine password. 
24.	An employee in your organization is suspected of sending important information to an accomplice outside the organization. The incident response team has intercepted some files from the employee's system that they believe have hidden information. You are asked to investigate a file named Confidential.txt and extract hidden information. Find out the information hidden in the file. Note: The Confidential.txt file is located at C:\Users\Admin\Documents in EH Workstation – 2 machine. 
25.	The incident response team has intercepted an image file from a communication that is supposed to have just text. You are asked to investigate the file and check if it contains any hidden information. Find out the information hidden in the file. Note: The vacation.bmp file is located at C:\Users\Admin\Documents in EH Workstation – 2 machine. 
26.	You are a malware analyst working for CEHORG. During your assessment within your organisation's network, you found a malware face.exe. The malware is extracted and placed at C:\Users\Admin\Documents in the EH Workstation – 2 machine. Analyze the malware and find out the File pos for KERNEL32.dll text. (Hint: exclude zeros.) 
27.	Analyze an ELF executable (Sample-ELF) file placed at C:\Users\Admin\Documents in the EH Workstation – 2 machines to determine the CPU Architecture it was built for. (malware module) 
28.	You have been given a task to audit the passwords of a server present in CEHORG network. Find out the password of the user Adam and submit it. (Note: Use Administrator/ CSCPa$$ when asked for credentials). 
29.	Use Yersinia on the “EH Workstation – 1” (Parrot Security) machine to perform the DHCP starvation attack. Analyze the network traffic generated during the attack and find the Transaction ID of the DHCP Discover packets. 
30.	CEHORG suspects a possible sniffing attack on a machine in its network. The organization has retained the network traffic data for the session and stored it in the Documents folder in EH Workstation – 2 (Windows 11) machine as sniffsession.pcap. You have been assigned a task to analyze and find out the protocol used for sniffing on its network. 
31.	As an ethical hacker, you are tasked to analyze the traffic capture file webtraffic.pcapng. Find out the packet's id that uses ICMP protocol to communicate. Note: The webtraffic.pcapng file is located at C:\Users\Administrator\Documents\ in the Documents folder on EH Workstation – 2 (Windows 11) machine. 
32.	An attacker has created a custom UDP packet and sent it to one of the machines in the CEHORG. You have been given a task to study the ""CustomUDP.pcapng"" file and find the data size of the UDP packet (in bytes). Note: The CustomUDP.pcapng file is located at C:\Users\Administrator\Documents\ in the Documents folder on EH Workstation – 2 (Windows 11) machine. 
33.	A denial-of-service attack has been launched on a target machine in the CEHORG network. A network session file "DoS.pcapng" has been captured and stored in the Documents folder of the EH Workstation - 2 machine. Find the IP address of the attacker's machine. 
34.	A machine in CEHORG network has been installed with a spyware by an Ex-employee. You are given a task to connect to the attacked machine to find out the hidden flag in the documents folder. 
35.	A disgruntled employee in CEHORG has used the Covert_TCP utility to share a secret message with another user in the CEHORG network. Covert_TCP manipulates the TCP/IP header of the data packets to send a file one byte at a time from any host to a destination. It can be used to hide the data inside IP header fields. The employee used the IP ID field to hide the message. The network capture file “Capture.pcapng” has been retained in the “C:\Users\Administrator\Documents” directory of the “EH Workstation – 2” machine. Analyze the session to get the message that was transmitted. 
36.	CEHORG has assigned you with analysing the snapshot of the operating system registry and perform the further steps as part of dynamic analysis and find out the whether the driver packages registry is changed. Give your response as Yes/No. 
37.	Perform windows service monitoring and find out the service type associated with display name "afunix". 
38.	CEHORG has found that one of its web application movies.cehorg.com running on its network is leaking credentials in plain text. You have been assigned a task of analysing the movies.pcap file and find out the leaked credentials. Note: The movies.pcapng file is located at C:\Users\Administrator\Documents\ in the Documents folder on EH Workstation – 2 (Windows 11) machine. Make a note of the credentials obtained in this flag, it will be used in the Part 4 of CEH Skill Check. 
39.	CEHORG hosts a datacenter for its bussiness clients. While analyzing the network traffic it was observed that there was a huge surge of incoming traffic from multiple sources. You are given a task to analyze and study the DDoS.pcap file. The captured network session (DDoS.pcapng) is stored in the Documents folder of the EH Workstation -2 machine. Determine the number of machines that were used to initiate the attack. 
40.	Perform an HTTP-recon on www.certifiedhacker.com and find out the version of Nginx used by the web server. 
41.	An FTP site is hosted on a machine in the CEHORG network. Crack the FTP credentials, obtain the “flag.txt” file and determine the content in the file. 
42.	Perform web application reconnaissance on movies.cehorg.com and find out the HTTP server used by the web application. 
43.	Perform a SQL Injection attack on movies.cehorg.com and find out the number of users available in the database. Use Jason/welcome as login credentials. 
44.	Identify the load balancing service used by eccouncil.org. 
45.	Identify the Content Management System used by www.cehorg.com. 
46.	Perform a bruteforce attack on www.cehorg.com and find the password of user adam. 
47.	Perform parameter tampering on movies.cehorg.com and find out the user for id 1003. 
48.	You have identified a vulnerable web application on a Linux server at port 8080. Exploit the web application vulnerability, gain access to the server and enter the content of RootFlag.txt as the answer. 
49.	You have been assigned a task to perform a clickjacking test on www.certifiedhacker.com that the CEHORG members widely use. Find out whether the site is vulnerable to clickjacking. 
50.	Perform command injection attack on 10.10.10.25 and find out how many user accounts are registered with the machine. Note: Exclude admin/Guest user 
51.	A 	file 	named 	Hash.txt 	has 	been 	uploaded 	through 	DVWA 
(http://10.10.10.25:8080/DVWA). The file is located in the directory mentioned below. Access the file and crack the MD5 hash to reveal the original message; enter the content after cracking the hash. You can log into the DVWA using the following credentials. Note: Username- admin; 
	Password- 	password 	Path: 
C:\wamp64\www\DVWA\hackable\uploads\Hash.txt Hint: Use “type” command to view the file. Use the following link to decrypt the hash- https://hashes.com/en/decrypt/hash 
52.	Perform Banner grabbing on the web application movies.cehorg.com and find out the ETag of the respective target machine. 
53.	Perform Web Crawling on the web application movies.cehorg.com and identify the number of live png files in images folder. 
54.	Perform XSS vulnerability test on www.cehorg.com and identify whether the application is vulnerable to attack or not. (Yes/No). 
55.	CEHORG suspects of a possible session hijacking attack on a machine in its network. The organisation has retained the network traffic data for the session at C:\Users\Admin\Documents in the EH Workstation – 2 as sniffsession.pcap. You have been assigned a task to perform an analysis and find out the protocol that has been used for sniffing on its network. 
56.	An attacker has intruded into the CEHORG network with malicious intent. He has identified a vulnerability in a machine. He has encoded the machine's IP address and left it in the database. While auditing the database, the encoded file was identified by the database admin. Decode the EncodedFile.txt file in the Document folder in the "EH Workstation – 2" machine and enter the IP address as the answer. (Hint: Password to decode the file is Pa$$w0rd) 
57.	The Access code of an employee was stolen from the CEHORG database. The attacker has encrypted the file using the Advance Encryption Package. You have been assigned a task to decrypt the file; the organization has retained the cipher file ""AccessCode.docx.aes"" in the Document folder in the ""EH Workstation – 2"" machine. Determine the access code by decrypting the file. Hint: Use ""qwerty"" as the decryption password. Note: 
Advanced Encryption Package is available at E:\CEH-Tools\CEHv12 Module 20 Cryptography\Cryptography Tools. 
58.	A VeraCrypt volume file "secret" is stored on the Document folder in the "EH Workstation – 2" machine. You are an ethical hacker working with CEHORG; you have been tasked to decrypt the encrypted volume and determine the number of files stored in the volume. (Hint: Password: test) 
59.	You have received a folder named "Archive" from a vendor. You suspect that someone might have tampered with the files during transmission. The Original hashes of the files have been sent by the sender separately and are stored in a file named FileHashes.txt stored in the Document folder in the "EH Workstation – 2" machine. Your task is to check the integrity of the files by comparing the MD5 hashes. Compare the hash values and determine the file name that has been tampered with. Note: Exclude the file extension in the answer field. The answer is case-sensitive. 
60.	CEHORG hosts multiple IoT devices and sensors to manage its supply chain fleet. You are assinged a task to examine the file "IOT Traffic.pcapng" located in the Home directory of the root user in the "EH Workstation - 1" machine. Analyze the packet and find the topic of the message sent to the sensor. 
61.	An employee in CEHORG has secretly acquired Confidential access ID through an application from the company. He has saved this information on the Downloads folder of his Android mobile phone. You have been assigned a task as an ethical hacker to access the file and delete it covertly. Enter the account information present in the file. Note: Only provide the numeric values in the answer field. 
62.	The mobile device of an employee in CEHORG has been hacked by the hacker to perform DoS attack on one of the server in company network. You are assigned to analyse "Andro.pcapng" located in Documents directory of EH workstation-2 and identify the severity level of the attack. (Note: perform deep down Expert Info analysis) 
63.	An attacker has hacked one of the employees android device in CEHORG and initiated LOIC attack from the device. You are an ethical hacker who had obtained a screenshot of the attack using a background application. Obtain the screenshot of the attack using PhoneSploit from the attacked mobile device and determine the targeted machine IP along with send method. 
64.	An 	attacker 	installed 	a 	malicious 	mobile 	application 
'AntiMalwarescanner.apk' on the victims android device which is located in EH workstation-2 documents folder. You are assigned a task to perform security audit on the mobile application and find out whether the application using permission to Read-call-logs. 
65.	An ex-employee of CEHORG is suspected to be performing insider attack. You are assigned a task to attain KEYCODE-75 used in the employees' mobile phone. Note: use option p in PhoneSploit for next page. 
66.	CEHORG hosts multiple IOT devices and sensors to manage its supply chain fleet. You are assinged a task to examine the file "IOT Traffic.pcapng" located in the Home directory of the root user in the "EH Workstation - 1" machine. Analyze the packet and find the topic of the message sent to the sensor. 
67.	CEHORG hosts multiple IOT devices and network sensors to manage its IT-department. You are assigned a task to examine the file "NetworkNS_Traffic.pcapng" located in the Documents folder of the user in the "EH Workstation - 2" machine. Analyze the packet and find the alert message sent to the sensor. 
68.	An attacker had sent a message 166.150.247.183/US to the victim. You are assigned to perform footprinting using shodan.io in order to identify whether the message belongs to SCADA/ICS/IoT systems in US. 
69.	An attacker had sent a file cryt-128-06encr.hex containing ransom file password, which is located in documents folder of EH-workstation-2. You are assigned a task to decrypt the file using cryp tool. Perform cryptanalysis, Identify the algorithm used for file encryption and hidden text. Note: check filename for key length and hex characters. 
70.	Username is john of WordPress website use msf wp scanner to find its password 
71.	There is secret file in window server 2019 and have backdoor installed find that file and paste contents 
72.	Which machine in the network has RDP service running? 
73.	Remote desktop to server 2019 and get a file present on desktop? 
74.	Use snow to unstego file and provide content 
75.	Use PCAP provided to find IP of attacking machine of DOS 
76.	Identify IP addresses of DDOS attack machines, how many they are in total 
77.	Use dsss.py to identify vulnerable sql link and paste the phone number of ketty 
78.	Which http method of website is vulnerable use owasp zap to identify? 
79.	A file is encrypted using des-ecb decrypt and find password and ip of ftp server, username is James 
80.	Hash is present at web link and find plain text using hashes.com 
81.	Domain controller has legitimate account already present name as john, Sam , administrator what other account exist other than this 
82.	Use BC text encoder to decode a file 
83.	Use hydra to break ftp and download file name as flag1.txt 
84.	Use crypt tool to decrypt account number having rc4 encryption with 14 as key length 
85.	Which machine in network has blind sqli and have mysql running? 
86.	Exploit weak credentials used for FTP service on a windows machine in the 192.168.0.0/24 subnet. Obtain the file, Credential.txt hosted on FTP root and enter its content as answer 
87.	Exploit the web application available at www.cehorg.com and enter the flags value at the page with page_id=84 
88.	Identify a machine with smb service enabled in 192.168.0.0/24 subnet. Crack the smb credentials for user Henry and obtain sniff.txt file containing an encoded secret. Decrypt the encoded secret and enter the decrypted text as answer. Note: Use Henry’s password to decode the text 
89.	A disgruntled ex employee has hidden a server access code in windows machine in 192.168.0.0/24 subnet. You can not physically access the target machine, but you know that the organization has installled RAT in machine for remote admin purpose. Your task is to retrieve the “sa_code.txt” file from target machine and enter the string in file as answer 
90.	Perform vulnerability research and exploit the web application training.cehorg.com available at 192.168.0.4. Locate tge Flag.txt file and enter its content as answer 
91.	During ana assessment an incident responser has retained a suspicious executable fike “die-another-day”. Your task as malware analyst is to find the executable entry point(Address). The file is in the C:\Users\Admin\Documents directory in “EH workstation-2” machines 
92.	Exploit a remote login and command line execution app on linux target in 192.168.0.0/24 subnet to access a sensitive file, NeyworkPass.txt. Enter the content in file as answer 
93.	An insider attack has been identified in one of the employees mobile device in 192.168.0.0/24 subnet. You are assigned to covertly access the users device and obtain malicious elf file stored in folder “scan”. Perform deep scan on the elf files and obtain the last 4 digits of SHA384 ash of file with highest entropy value 
94.	Perform vulnerability scan for host with ip address 172.20.0.16 what is the severity score of vulnerability that indicates the end of life of web development language platform? 
95.	Perform SQL injection attack on web application cybersec.cehorg.com available at 172.20.0.22 Find the value in Flag column in one of DB tables and enter it as answer 
96.	Your organization suspects the presence of a rogue AP in the vicinity. You are tasked with cracking the wireless encrypt connecting te network and set up a oenypot. The airdump-ng tool has used and the wifi trafiic capture named “WirelessCapture.cap” is located in Document folder in “EH Workstation1” machine. Crack the wireless encrypt and identify the wifi password 
97.	You used shoulder surfing to identify the username and password of user on ubuntu in 192.168.0.0/24 network that is smith and L1nux123. Access the target machine perform vertical privilege escalate to that root user and enter the content of imroot.txt file as answer 



⚠️ Disclaimer / Descargo de Responsabilidad
Español: Todo el material, enlaces y comentarios proporcionados en este documento tienen fines estrictamente educativos y de aprendizaje. El uso de esta información es responsabilidad exclusiva del usuario. No se garantiza la pertinencia, exactitud o actualidad del material entregado, ni se asegura el éxito en el examen oficial basado únicamente en este contenido. CEH y EC-Council son marcas comerciales registradas de International Council of E-Commerce Consultants (EC-Council). Este documento no está afiliado, patrocinado ni aprobado por EC-Council.

English: All materials, links, and comments provided in this document are strictly for educational and learning purposes. The use of this information is the sole responsibility of the user. There is no guarantee regarding the relevance, accuracy, or timeliness of the material provided, nor is success in the official exam ensured based solely on this content. CEH and EC-Council are registered trademarks of the International Council of E-Commerce Consultants (EC-Council). This document is not affiliated with, sponsored by, or endorsed by EC-Council.




