# Installing embarcadero mind machine

To install embarcadero mind machine manually, use the 
normal `setup.py` procedure:

```
git clone https://github.com/rainbow-mind-machine/embarcadero-mind-machine.git
cd embarcadero-mind-machine
python setup.py build 
python setup.py install
```

To install embarcadero mind machine with pip:

```
pip install embarcaderomindmachine
```

## Required Packages

If you need a list of required packages, see `requirements.txt`.
These packages will be installed using either of the above 
installation methods.

# What You Need to Run a Bot Flock

You will need a few additional things before you can get a bot flock
up and running with embarcadero mind machine.

## A Bot Idea

You will need to decide on the behaviors
you want the bot to have, so you know how to 
structure the bot repository, what data to include,
and how to extend Sheep and Shepherd.

You will be defining how the Sheep 
(one sheep = one bot)
will populate their tweet queues.
This may be a simple action (get an item 
from a list owned by the Sheep), 
or it may be a complicated one
(make a URL request to get live data,
query a database, call an API, etc.).

See [`example_flocks/`](/example_flocks).

## Bot Master Account

It's good practice to create the OAuth application 
you'll be using to run your bot flock under a bot master account.

Like your OAuth application, the bot master account 
can be used to run as many bot flocks as you would like,
so you don't need to make it flock-specific.

This account is also (obviously) not itself a bot,
so you can use your personal twitter account 
as the bot master account.

## Bot Accounts

embarcadero mind machine handles everything _but_ the creation of bot accounts. 
You must already have created a user account for each bot.

No customization of the bot accounts is needed 
prior to using embarcadero mind machine.


## An OAuth App

You also need to create an OAuth application.
You can use one application across all of your 
bot flocks - there is no limit on the number of 
accounts a single application can control.

It is recommended you create this app using a 
"bot master" account, and not using the bot 
accounts themselves.

This will register your embarcadero mind machine bot flock 
application with Github, and give you credentials 
(one token and one secret token)
that will allow you to connect to Github's API
as the mind machine application that you are 
about to build.

When you register your application you will get a token
and a secret token. These are provided to the Keymaker.
(See [boring mind machine](https://pages.charlesreid1.com/boring-mind-machine/).)

