# World Wide Torrents Uploader (WWT Uploader) [![N|Solid](http://i.imgur.com/RwF2IVH.png)](http://worldwidetorrents.eu/)

A little python script made to upload torrents on worldwidetorrents.eu by making use of their API upload. This is a very basic script which can upload multiple torrents to WWT. However, the description and category of those torrents will be same. You can of course change the description and category id if you upload one torrent at a time.

  - Multiple Torrents can be uploaded.
  - Custom description allowed.
  - Supports BBCODE in descriptions.
  - Files with special characters in name can be uploaded.

> Idea was suggested by a lazy bastard.

You will need curl.exe for this to work. Just clone this repository and you'll get curl in it. This script is supported by both, python 2 and 3.

## Table of Content

* [Things to do First](#things-to-do-first)
* [List of Arguments](#list-of-arguments)

Check the [Release Section](https://github.com/Xonshiz/WWT-Uploader/releases) for windows binary. As usual, it's a 32 bit binary and hence, it should run on both x64 and x86 systems.

## Things to do First
First, sign up on [WWT](https://worldwidetorrents.eu/account-login-signup.php) and register yourself for an api [by going here](http://worldwidetorrents.eu/api/).

After WWT staff validates you API request, you'll receive an API KEY on [this page](http://worldwidetorrents.eu/api/). Keep in mind that this is very important and this key should be treated like your password. Anyone with your key can upload torrents from your account.

Then, you need to know torrent category id, which you can [see on their category list page](http://worldwidetorrents.eu/catlist.php).We need the numerical value for the category id. or you can pass the `--id` argument to this script and see the list.

## List of Arguments
Currently, the script supports these arguments :
```
-h, --help                          Prints the basic help menu of the script and exits.
--version                           Shows version and exits.
--id                                Shows version and exits.
--setup                             Starts a setup for making an INI file.
```

## How To Use :

### Part 1:
The script makes a `settings.ini` file and stores the information in that. So, to generate that, you need to run the script with `--setup` function.

1.) First, open the "`Description.txt`" file and enter your desired description in it and save the file (save it in the same directory).

2.) Open a shell/Command prompt and go to the directory/folder where this script is. Now, type `__main__.py --setup` (if you're using py file) or type `WWT_Uploader.exe --setup` (If you're using windows binary).

3.) It'll ask for your Api key. So, paste your API Key here.

4.) It will now ask for `category id` of the torrent. Enter the id number that you found out before.

If you provided correct information, correctly, then this should generate a settings.ini file. Now, later if you feel the need to change the torrent category id, then you can make change in the settings.ini file directly. But, you need to be very careful while making changes in the description section of settings.ini file. Keep the tab space maintained (it's advised to use --setup when you want to update anything though).

### Part 2:
Now, after generating a settings.ini file, you're ready to use this script. Just follow these steps now :

1.) Copy the .torrent file(s) you want to upload to WWT into the directory of this script.

2.) Open a shell/Command prompt and go to the directory/folder where this script is. Now, type `__main__.py` (if you're using py file) or type `WWT_Uploader.exe` (If you're using windows binary).

Now, the script will begin uploading the torrent to WWT and would show the message on the command prompt/shell.

You don't have to follow part 1 everytime. You can just go to part 2 if you don't have to make major changes to description or category id.