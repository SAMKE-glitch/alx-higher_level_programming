JavaScript - Web jQuery

For this project, we expect you to look at these concepts:

JavaScript in the browser()

JavaScript in the browser
Why JavaScript in the browser?
Now that we can structure the document and its content with HTML, and that we can style it in many ways with CSS, we may want to go beyond those capabilities (dynamically change the HTML document, perform some operations based on some current circumstances, …). JavaScript was created with exactly that goal in mind, and is still being used as such; its recent popular renewal as a language for scripts and web back-ends using Node.js is quite recent. All browsers expect HTML, CSS and JavaScript; Whatever you want to write for the web, even the most complex applications (even GMail, Google Maps, …) will have no choice but to be composed of those three technologies if they want to be understood by browsers.

A quick history to know where we come from
Note: the JavaScript language has nothing to do with the Java language. Please make sure not to use the wrong word!

Step 1: Browser War and standardization
Before the Browser War, the first “mainstream” browser was called Mosaic. It existed between 1993 and 1997 and had very limited features. Netscape released Netscape Navigator in 1995 in an attempt to shake things up and bring more features to the web experience. Quickly, Netscape Navigator had ~80% market share; but then quickly came Microsoft Internet Explorer 1.

The Browser War was a time when web browser market share was shared between Netscape Navigator and Microsoft Internet Explorer, and each browser was trying to one-up the other with fancy features for developers. It is a time that saw the birth of frames, CSS, and… JavaScript! Brendan Eich, back then a developer at Netscape, wrote the first version of JavaScript in 10 days (and it kinda still shows in the quirks of the language!), in order to ship it before Internet Explorer, with almost no documentation. People making websites were quick to use it to do nice things with Netscape Navigator, so Microsoft shipped a reverse-engineered version of it a few days later.

Of course, with this kind of approach, behavior in browsers were inconsistent, so Netscape ended up submitting the language for standardization with the ECMA, where it was given its actual name: ECMAscript (but everybody keeps saying JavaScript, so you should keep calling it that too).

Step 2: shy steps towards consistency
Netscape Navigator 5 was taking far too long to build because of heavy legacy issues, so Netscape decided to give it up and to prepare for Netscape Navigator 6, rebuilt entirely from the ground up. Rebuilding something this large entirely from the ground up is notoriously always a very bad decision in product management, and this occurrence didn’t fail the rule: Netscape disappeared for years while its browser took much longer than expected to be built, making a boulevard for Microsoft Internet Explorer to take virtually all of the market share.

The result for JavaScript is that for years, Microsoft didn’t follow through on their promise to make their version of JavaScript compatible with the ECMA standard. They had good reasons not to: since almost the entire planet was using their product, their incompatibility with other browsers was kind of a competitive advantage. Since developers who could only focus their efforts on one version of JavaScript were focusing on Microsoft Internet Explorer, their websites were effectively broken in other browsers.

This gave birth to Javascript libraries whose goals were to harmonize a single language API that worked in all browsers, such as JQuery (which comes with other features too).

Step 3: towards a more mature language
After years of JavaScript developers having to either produce one code per browser, or use libraries like JQuery, Microsoft’s strategy eventually caught up to them for two main reasons:

Rich front-end applications requiring heavy JavaScript became more and more mainstream, and Microsoft’s willful years of tardiness compared to other browsers led Internet Explorer (circa version 6, 7 and 8) to be much slower than the rest of the competition. People started to install other browsers in order to use comfortably their Gmail, Google Maps, etc.
Microsoft’s behavior was so obviously anti-constructive that they got a ton of lawsuits from competitors and from governments, most of which they lost. One of the most painful outcomes for them was the “ballot screen”: they had to display a screen on installation presenting their competing browsers to all of their European customers. This led European users to even more migrate to other browsers. This was a wake-up call for Microsoft, which reconsidered entirely their strategy, and came up with Internet Explorer versions (circa version 9 or 10) that were finally reasonably compatible with all relevant specs, and with JavaScript engine speeds comparable to their competitors. More recently, to make Internet Explorer and its terrible reputation a thing of the past, they have rebranded it as “Microsoft Edge”, and adopted a much more open strategy.
Microsoft 180-degre shift was immensely beneficial to JavaScript for browsers, since the same JavaScript code can now be ran transparently on all browsers with little risk; also, now that the whole industry is caught up, JavaScript’s pace of standardization for new features has dramatically increased within the past few years, and JavaScript is slowly becoming less and less like the quirky language that was created in 10 days as a marketing stunt in the mid-90s, and more and more like a modern, full-featured language.

JQuery & co
While JQuery’s syntax is very appreciated by developers, one of its obvious tradeoffs is one of performance: all of your users are loading and running a library bringing a ton of features, while you might only need a handful.

It used to make obvious sense up until recently, but JQuery’s two main upsides are now eroding:

It was immensely useful in writing code to safely work on all browsers; but now that Microsoft has caught up and is “fighting” for Microsoft Explorer < 9 to disappear from their clients’ computers, this has become less and less a problem as those browsers disappear.
Even today, it makes quite a few annoying and/or verbose Javascript syntaxes (such as making an Ajax call, or “selecting” an HTML element) much more developer-friendly. But for the newest versions of ECMAscript, many JQuery syntaxes have been used as inspiration and are directly offered in native “vanilla” JavaScript.
Even though JQuery is still heavily used in a lot of production websites, developers are much more prompt to reconsider using it in their websites if they only need a handful of features (see the website called “You might not need JQuery”, offering easy solutions in native “vanilla” JS to reproduce the most used features in JQuery).

A more lightweight and recent library that has been popular is Underscore.js, which was later forked as another project called lodash (got the pun?). It only attempted to make JavaScript’s syntax less verbose (and didn’t attempt to solve the browsers’ inconsistencies). Since they do not intend to tackle the differences between browsers, they are as relevant when using JavaScript in the browser as with Node.js. Maybe someday, ECMAscript will catch up to the syntactic sugar offered by Underscore and lodash, but waiting for this, they are quite popular today, and should remain so in the foreseeable future.

Some feats of JavaScript in the browser
Now that you’re amazingly comfortable with JavaScript in Node.js (!!!), you might wonder what the differences are between the JavaScript you’ve experienced there and the JavaScript you’re going to experience in the browser. Here are some differences:

The JavaScript version In Node.js, if a new version of JavaScript is stabilized, then you can update Node.js on your computer/server, and suddenly, you can use the latest fancy features of JavaScript. In the browser, you know nothing about the engine running your code, since it’s the user’s browser. They might be running a very old browser, that doesn’t understand the latest features. Therefore, most recent upgrades to JavaScript are not usable by front-end developers for months or years. Use the “Can I use?” website to find out what features are reasonably implemented by browsers.

The “special” objects The browser is giving you access to its features through a number of objects, like the window object, which represents the browser tab this code is running in, the navigator object, giving information about the browser used in general, etc. Most of those APIs are not standardized, but they are typically the same across browsers.

The DOM Standing for “Document Object Model”, the DOM is the HTML code as the browser “understands” it, i.e. as a tree. If you’re uncomfortable with why your browser thinks of your HTML code as a tree, you should read this: What is the Document Object Model?. The browser comes with the DOM API, which allows you to travel through the tree as needed: find elements in it, add or remove nodes, travel up or down the tree, … Those APIs are made available through the document object, representing the HTML document in which the code runs.

The event-orientation Since JavaScript in the browser is meant to perform actions when certain things happen, callbacks are not being run after I/O operations are performed like in Node.js, but when some events happen. Those events can be triggered by the user (a click on a button, the browser window being resized, …) or sometimes not (an image isn’t loading properly, the HTML webpage has finished loading, …)

Tools
You have many features in your browser’s dev tools meant to help you: a JavaScript console where you can run code that will directly apply to the webpage that is opened, a debugger allowing you to add breakpoints, etc. Take some time to get familiar with them…


Dealing with data statically versus dynamically()
Dealing with data statically versus dynamically
We often use the terms “static” and “dynamic” when it comes to websites. A static website is unchanging and stays the same regardless of how we interact with it. A dynamic website has content and/or presentation that can change (courtesy of scripts that loads every time the site is loaded). The same static-dynamic concept can be applied to data handling. If you deal with data statically, you’re using your dataset as a fixed set of values; if you deal with data dynamically, you’re using it as a set of data that changes over time.

In today’s project you have a choice about how to handle the data: dynamically or statically. For instance, if you wanted to have a bar chart of the number of tech workers relative to other workers living in San Francisco, and you wanted this chart to always pull from the latest data on SF Open Data, you’d want your code to fetch, parse, and compute the data every time your visualization is rendered. On the other hand, if you wanted bar charts that show the ratio of workers at specific points in time (e.g., 5 years ago compared to now), there’s really no point fetching, parsing and computing the data every time your visualization is rendered. You just need to download or pull the data to your local server, compute the numbers you want, and add it to your Javascript one time. This means that you are working with a static set of data.

Resources
Read or watch:

What is JavaScript?(https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript)
Selector(https://jquery-tutorial.net/selectors/using-elements-ids-and-classes/)
Get and set content(https://jquery-tutorial.net/dom-manipulation/getting-and-setting-content/)
Manipulate CSS classes(https://jquery-tutorial.net/dom-manipulation/getting-and-setting-css-classes/)
Manipulate DOM elements(https://jquery-tutorial.net/dom-manipulation/the-append-and-prepend-methods/)
API(https://oscarotero.com/jquery/)
Introduction(https://jquery-tutorial.net/ajax/introduction/)
GET & POST request(https://jquery-tutorial.net/ajax/the-get-and-post-methods/)
JQuery Ajax Tutorial #1 - Using AJAX & API’s(https://www.youtube.com/watch?v=fEYx8dQr_cQ&ab_channel=LearnCode.academy)
What went wrong? Troubleshooting JavaScript(https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_went_wrong)
JQuery(https://jquery.com/)
JQuery API(https://api.jquery.com/)
JQuery Ajax(https://learn.jquery.com/ajax/)


Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
Why JQuery make front-end programming so easy (don’t forget to tweet today, with the hashtag #ilovejquery :))
How to select HTML elements in JavaScript
How to select HTML elements with JQuery
What are differences between ID, class and tag name selectors
How to modify an HTML element style
How to get and update an HTML element content
How to modify the DOM
How to make a GET request with JQuery Ajax
How to make a POST request with JQuery Ajax
How to listen/bind to DOM events


0. Write a JavaScript script that updates the text color of the <header> element to red (#FF0000):

You must use document.querySelector to select the HTML tag
You can’t use the JQuery API
Please test with this HTML file in your browser:

guillaume@ubuntu:~/0x15$ cat 0-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="0-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

1. Write a JavaScript script that updates the text color of the <header> element to red (#FF0000):

You can’t use document.querySelector to select the HTML tag
You must use the JQuery API
Please test with this HTML file in your browser:

guillaume@ubuntu:~/0x15$ cat 1-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="1-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

2. Write a JavaScript script that updates the text color of the <header> element to red (#FF0000) when the user clicks on the tag DIV#red_header:

You can’t use document.querySelector to select the HTML tag
You must use the JQuery API
Please test with this HTML file in your browser:

guillaume@ubuntu:~/0x15$ cat 2-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="2-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

4. Write a JavaScript script that adds the class red to the <header> element when the user clicks on the tag DIV#red_header

You can’t use document.querySelector to select the HTML tag
You must use the JQuery API
Please test with this HTML file in your browser:

guillaume@ubuntu:~/0x15$ cat 3-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <style>
      .red {
        color: #FF0000;
      }
    </style>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="3-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

5. Write a JavaScript script that toggles the class of the <header> element when the user clicks on the tag DIV#toggle_header:

The <header> element must always have one class: red or green, never both in the same time and never empty.
If the current class is red, when the user click on DIV#toggle_header, the class must be updated to green ; and the reverse.
You can’t use document.querySelector to select the HTML tag
You must use the JQuery API
Please test with this HTML file in your browser:

guillaume@ubuntu:~/0x15$ cat 4-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <style>
      .red {
        color: #FF0000;
      }
      .green {
        color: #00FF00;
      }
    </style>
  </head>
  <body>
    <header class="green"> 
      First HTML page
    </header>
    <div id="toggle_header">Toggle header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="4-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15

5. Write a JavaScript script that adds a <li> element to a list when the user clicks on the tag DIV#add_item:

The new element must be: <li>Item</li>
The new element must be added to UL.my_list
You can’t use document.querySelector to select the HTML tag
You must use the JQuery API
Please test with this HTML file in your browser:

guillaume@ubuntu:~/0x15$ cat 5-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="add_item">Add item</div>
    <br />
    <ul class="my_list">
      <li>Item</li>
    </ul>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="5-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15

6. Write a JavaScript script that updates the text of the <header> element to New Header!!! when the user clicks on DIV#update_header

You can’t use document.querySelector to select the HTML tag
You must use the JQuery API
Please test with this HTML file in your browser:

guillaume@ubuntu:~/0x15$ cat 6-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="update_header">Update the header</div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="6-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$

7. Write a JavaScript script that fetches the character name from this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json

The name must be displayed in the HTML tag DIV#character
You can’t use document.querySelector to select the HTML tag
You must use the JQuery API
Please test with this HTML file in your browser:

guillaume@ubuntu:~/0x15$ cat 7-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      Star Wars character
    </header>
    <br />
    <div id="character"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="7-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

8. Write a JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json

All movie titles must be list in the HTML tag UL#list_movies
You can’t use document.querySelector to select the HTML tag
You must use the JQuery API
Please test with this HTML file in your browser:

guillaume@ubuntu:~/0x15$ cat 8-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      Star Wars movies
    </header>
    <br />
    <ul id="list_movies">
    </ul>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="8-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

9. Write a JavaScript script that fetches from https://fourtonfish.com/hellosalut/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello.

The translation of “hello” must be displayed in the HTML tag DIV#hello
You can’t use document.querySelector to select the HTML tag
You must use the JQuery API
Your script must work when it is imported from the <head> tag
Please test with this HTML file in your browser:

guillaume@ubuntu:~/0x15$ cat 9-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="9-script.js"></script>
  </head>
  <body>
    <header> 
      Say Hello!
    </header>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

10. Write a JavaScript script that updates the text color of the <header> element to red (#FF0000):

You must use document.querySelector to select the HTML tag
You can’t use the jQuery API
Note: Your script must be imported from the <head> tag, not at the end of the HTML
Please test with this HTML file in your browser:

guillaume@ubuntu:~/0x15$ cat 100-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script type="text/javascript" src="100-script.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

11. Write a JavaScript script that adds, removes and clears LI elements from a list when the user clicks:

The new element must be: <li>Item</li>
The new element must be added to UL.my_list
When the user clicks on DIV#add_item: a new element is added to the list
When the user clicks on DIV#remove_item: the last element is removed from the list
When the user clicks on DIV#clear_list: all elements of the list are removed
You can’t use document.querySelector to select the HTML tag
You must use the JQuery API
You script must work when it imported from the HEAD tag
Please test with this HTML file in your browser:

guillaume@ubuntu:~/0x15$ cat 101-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="101-script.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="add_item">Add item</div>
    <div id="remove_item">Remove item</div>
    <div id="clear_list">Clear list</div>
    <br />
    <ul class="my_list">
      <li>Item</li>
    </ul>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

12. Write a JavaScript script that fetches and prints how to say “Hello” depending on the language

You should use this API service: https://www.fourtonfish.com/hellosalut/hello/
The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.)
The translation must be fetched when the user clicks on INPUT#btn_translate
The translation of “Hello” must be displayed in the HTML tag DIV#hello
You can’t use document.querySelector to select the HTML tag
You must use the JQuery API
You script must work when imported from the <head> tag
Please test with this HTML file in your browser:

guillaume@ubuntu:~/0x15$ cat 102-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="102-script.js"></script>
  </head>
  <body>
    <header> 
      Say Hello
    </header>
    <br />
    <input id="language_code" type="text" placeholder="Language code"/>
    <input id="btn_translate" type="button" value="Translate"/>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

13. Write a JavaScript script that fetches and prints how to say “Hello” depending on the language

You should use this API service: https://www.fourtonfish.com/hellosalut/hello/
The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.)
The translation must be fetched when the user clicks on INPUT#btn_translate OR presses ENTER when the focus is on INPUT#language_code
The translation of “Hello” must be displayed in the HTML tag DIV#hello
You can’t use document.querySelector to select the HTML tag
You must use the JQuery API
You script must work when imported from the <head> tag
Please test with this HTML file in your browser:

guillaume@ubuntu:~/0x15$ cat 103-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="103-script.js"></script>
  </head>
  <body>
    <header> 
      Say Hello
    </header>
    <br />
    <input id="language_code" type="text" placeholder="Language code"/>
    <input id="btn_translate" type="button" value="Translate"/>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
