# 👻GhostPost 👻
 The GhostPost Machine™ is a website where people can anonymously post Boasts or Roasts of whatever they want. Like most services, there is a character limit: 280 characters. We are deliberately not dealing with logins, as that is outside the scope of the project (and beyond our time constraints). 

A front end is necessary to make this work, though it doesn't have to be pretty -- invest as much time as you want into it (assuming your application already has the requested features 🤓).

#### **Your Task**

Create a Django application with the following features.

Back end:

*   <span>One model to represent both boasts and roasts</span>
    *   <span>Boolean to tell whether it's a boast or a roast</span>
    *   <span>CharField to put the content of the post in</span><span></span>
    *   IntegerField for up votes
    *   IntegerField for down votes
    *   DateTimeField for submission time

Front end: 

*   Homepage that displays boasts and roasts, sorted by time submitted (hint --> [https://docs.djangoproject.com/en/3.0/ref/models/querysets/#order-by](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#order-by))
*   Buttons to filter the content by either boasts or roasts, sorted by time submitted
*   Upvote and downvote buttons for each boast and roast
    *   when clicked, these buttons affect the numbers on the relevant post appropriately
*   Ability to [sort](https://docs.python.org/3/howto/sorting.html#key-functions) content based on vote score (_hint:_ you may need to calculate the vote score) 
*   Page to submit a boast or a roast

Hints:

*   button hrefs can use template data, just like everything else
*   voting is not meant to be secure; this is effectively a proof of concept application
*   you do not need to worry about figuring out if someone has already voted on something

**Extra credit (7 points):**

*   Add a post deletion method that works for both boasts and roasts on the detail page. "Wait, how will we delete if it's anonymous?", I hear you ask. When a boast or a roast is created, it should have a random 6 character string associated with it (so that it's hard to guess). Every post now has two URLs... but one is public and one is private. For example, a valid post could have these two URLs:
    *   localhost:8000/posts/1
    *   localhost:8000/posts/abcdef
*   The one that ends in an ID should display a "public" version of the detail page; just the post itself. The one that ends in the "secret key" should be the same content, but with an additional button that allows you to delete the content. (Hint: have the button link to a different view that can delete a post by ID)
*   <span>When the object is created, the magic string should be passed back to the front end in a link and given to the user; something like "Keep this link secure; this is your private link for managing this post!"</span>

#### **Submission**

Submit a link to your repo.

<pre>https://github.com/ka-se-q4/ghostpost-&ltgithub_username&gt</pre>
