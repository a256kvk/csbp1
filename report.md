LINK: https://github.com/a256kvk/csbp1

FLAW 1:
https://github.com/a256kvk/csbp1/mysite/models.py#L19
CSRF (cross-site request forgery)
There is a CSRF vulnerability in updating private notes. A malicious website can send a POST request (for example a hidden form) to the website (http://localhost:8000/private_notes/) and overwrite the private notes if the user is logged in on the target website (http://localhost:8000). For example if you run `python -m http.server 8080` in the directory with csrf_attack_demo.html and go to "http://localhost:8080/csrf_attack_demo.html", it automatically does this (has an invisible form that is automatically sent using JavaScript and does the CSRF attack and overwrites the user's notes). Note that this only works if you are logged in. Note that this doesn't work (at least in my browser) if you just manually open the HTML file in your browser on your computer normally.



FLAW 2:
{link to source}
These flaws are from OWASP top 10 2017 (https://owasp.org/www-project-top-ten/2017/) and this flaw is flaw number 3, Sensitive Data Exposure.
When registering, the register form makes a GET request instead of a POST request. This also means that the password is sent via GET parameters, which show after the url and the url is like: http://localhost:8000/register/?csrfmiddlewaretoken=something&username=lol&password1=adsf&password2=adsf. The flaw is that these parameters usually get logged in the browser and in some cases on the server. This means that the password exists as plaintext on the client's computer.

FLAW 3:
Broken access control (A5:2017)
When deleting a post, it is not checked on the server if the user has the permissions to delete the post (i.e. it is not checked if the post was made by the user). This means that it is possible for someone to just delete any post on the site by for example just changing the hidden input field that specifies the post id that is going to get deleted to any arbitrary id and sending the request.

(note the @login_required)

FLAW 4:
Injection (A1:2017)
The search functionality for users is vulnerable to an SQL injection. Note that this is a read only SQL injection since the execute function only allows for executing one statement.
For example, the following query string inside parenthesis (' AND 1=0 UNION SELECT account_id, content FROM mysite_privatenotesmodel WHERE '%'=') (demonstrated in screenshot )steals the private notes of all the users associated with the user ids and the link even works and links to correct the user's page. This vulnerability can be used to steal for example the password hashes of the users, the session keys / session data of users, which can be used to do session hijacking. 

FLAW 5:
Cross-Site Scripting (XSS) (A7:2017)
In the View raw functionality, the server sends the contents of a post in a http response. However, the type of this response isn't specified as plain text, which means that in django the default type is HTML. This means that the browser views the response as HTML, which can include for example malicious JavaScript code.
