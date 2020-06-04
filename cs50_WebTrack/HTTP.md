### TPC / IP (Protocol) | HTTP (Protocol)
* Transmission Control Protocol / Internet Protocol, and these are the protocols that determine how it is that computers are able to communicate with one another over the internet.
* How does it work? You can think of it as analogou as sening a letter in an envelope for example. We have one envelope here that we want to send from one computer to another (fisically, one address to another), what information needs to go on that envelope for us to be able to know who we're sending information to, or make sure that envelope can get to the right place.
* In a real envelope, you need the name and address of the **Recipient**, and you also put on the envelope the **sender** with it's address.
* Computers have **IP Addresses**: ```#.#.#.#```, which all numbers in the **#** range from 0 to 255, or else, 8 bits of information each, which makes a total of 32 bits to work with, and this format is known as **IPv4**.
* We now have a newer protocol, the **IPv6**, which uses 128-bit addresses, instead os 32, allowing for far more addresses that can be available on the internet.
* What other information do we need other than the Addresses? Image a computer has some IP Address, that allows other computer send them messeges over the internet, and that computer might be receiving a whole bunch of **different types of messages** (Like Emails, WebPages, File Transfer), and the computer need some way of knowing how to distinguish between all of these different types of packages of information, is this package of information an Email, or is this package of information a WebPage? This is important, relevant information that this devide needs to know about. So, in order to solve that problem, **we assign** each of the different services of information, like Email or WebPages, or FileTransfers **a number**, and that number is called a **Port Number**: 

| Service   |      Port      | 
|----------|:-------------:|
| FTP (File Transfer Protocol) |  21 | 
| SMTP (Used for Email) |    25   | 
| HTTP (WebPages) | 80 | 
| ... | ... | 

* So what goes into the envolope than, is not just the **IP Address** of the destination, but also a **Port Number**.
    * Example: ``` 1.2.3.4:80 ```. so, 1.2.3.4 is the IP Address of who you want to send the message to, and 80 in this case indicating HTTP, which means we're sending a WebPage, from one computer on the internet, to another.
---
### DNS
* But these IP Addresses are not what we are normally interacting with, when typing addresses on then internet. Indeed, we're not typing IP Addresses, we're more commonly typing a **URL**, something like **http://www.example.com**, but how this URL connects to the specific IP Address we want to connect? In order to do this translation, we use what is called **DNS (Domain Name System)**, and DNS really is just a mapping between the **URLs** and their corresponding **IP Address**:

| URL   |      IP Address      | 
|----------|:-------------:|
| google.com |  172.217.7.206 | 
| harvard.edu |    23.22.75.102   | 
| yale.edu | 104.16.243.4 | 

* It woudl be really annoying every time you want to visit a website, you needed to know the IP Address of the server on which that WebSite is being served from. It's much easier to remember something like **harvard.edu**. So DNS is a bunch of Servers, these DNS servers exists on the internet that know for any particular URL, what IP Address does it correspond to. And so when you type something like google.com on your Webbrowser, your WebBrowser can check with the DNS server, and say what is the IP Address of google.com, and once it knows the IP Adrress, then your computer is enabled to communicate with google.com and request google.com webpage from there.
---
### HTTP
* HTTP stands for Hypertext Transfer Protocol, what HTTP is all about really, is what's inside of these envelopes, what is the content of a request that I send to a webpage, and what is the content of the response? When I make a request, it may look something like this:
```
GET / HTTP/1.1
Host: www.example.com
...
```
* **GET** is what is called a **Request Method**, and it means that I'm trying to get a Web Page.
* Next comes the **/**, and this second part is specifying what particular resource on the Webpage that I'm trying to connect to, do I want to get back. So many websites like google.com, for example, will have a **/search** or **/settings**, any number of other pages that I might try to access, so this **/** in this case is specifying that I want the root of the website.
* Following that there is the **HTTP/1.1**, this is specifying which version of the HTTP protocol I'm using, in order to communicate with this host. In this case I'm using version 1.1, which is quite common, nowadays version 2 is pretty common to.
* And beneath that I'm connecting to a particular Host, something like www.example.com, as the host that I want to communicate with. It's possible that the webserver that I'm communicating with is actually holding multiple hosts alltogether, so in my request I need to specify what host do I want to connect to, in this case, www.example.com.
* And there's more information that comes in the request other than that, but the key ideas here is that I'm trying to get a page from a particular host, I specify what page I want to access and I specify which version of HTTP Im currently using in order to make this request to the website.
* What then responds back to me, when www.example.com receives my requests and wants to send something back to me, the person who requested this page in the first place. The response might look something like this:
```
HTTP/1.1 200 OK
Content-Type: text/html
```
* Again, first the HTTP with its version. Then, a number, what is called a **Status Code**. Every time HTTP gives a response, it's coming with some code that specifies how the response was resolved, and 200 means that everything was OK (we're able to successfully send you back a response).
* The second line of the response specifies what type of response was returned back, in this case, **text/html**, some markup that is going to represent a WebPage.