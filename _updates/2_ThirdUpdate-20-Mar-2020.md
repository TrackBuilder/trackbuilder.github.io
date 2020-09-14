---
post_time: "20th Mar 2020:"
title: "Third update. Post demo procrastination. Corona time struggle. Steam page is up!"
excerpt: "2020-03-20 - Progress update"
toc: true
layout: posts
feature_image_path: "/assets/2020-03-20/serving.gif"
---

## 2 players, 3 maps and a buy menu.

![image.png](/assets/2020-03-20/serving.gif)

![image_2.png](/assets/2020-03-20/buying_1.gif)

-----------------------
### Fri Mar 20 00:12:03 2020 +0200

### [Tue 10/3: 5hr][1hr today]I have been super lazy in procrastinate lately. I was a bit burn out after the demo, so I though I could take a day off or two. Today: update the website.
And then the Corona came and then there is the whole work place shut-down and then I have to set up some remote work.

And I was mostly looking for a car to buy so we can avoid public transport during this pandemic time, ofcourse we try to stay home as much as possible, but sometimes, you have to go out.

But yeah, it was mostly procrastination as most night, I was just watching films with my wif. We finished the first season of Sex Education on Netflix, it was briliant, play a lot of Slay the spire, and like 2 or 3 nights just seeing old cars.

Hopefully, this update will be the back to action. I will try to focus on the game tomorrow.

The last week Tuesday demo went well. I had like 10 players played the game and I received a lot of notes and feedback. There was 2 guys who was genuelly enjoy the game and once they get the gasp, they played for quite a while and enjoy themselves quite a lot. So I guess I have something. Still lots of work to be done though, but it's great. I will probably need another update for all the updates I gathered.

Also, update, by now, I have 25 wishlists, after one and a half week on Steam, which is a bit too little. I guess the game is too early so not a lot of people interested in it, just yet. Let's see the update after a month, more graphic and stuffs.

-----------------------
### Tue Mar 10 00:37:26 2020 +0200

### [4hr]Add tons of duct tape so that the game is playable. Containing: buy menu, rework food container, 2 players mode and tons of duct tape.

Buy Menu: You can buy stuffs from the computer. You can also start game using that game menu as well. Using money, gain from serving customer.

Food container rework: Each food container spawner (POT/BOWL) will spawn only 1 bowl. More balance.
2 players: two players!

-----------------------

### Mon Mar 9 01:30:03 2020 +0200

[1.5hr]Spiritual commit as I don't really do much code. Just finish the steam page for the 3rd time. Let's hope that this time I didn't fuck up and I will finally have a steam page for the demo day.

-----------------------

### Sun Mar 8 23:58:54 2020 +0200

[2hr]Start working on the computer to buy sell stuffs. The computer works at the basic level as I press it, and it will show a buy menu, but there's nothing yet. Will need to design and balance it. But now, I will head to prepare the steam page.

-----------------------
### Sun Mar 8 15:24:40 2020 +0200

### [3hr]Start menu and restart game function seems to work. Next to working on the Computer to have a SELL/BUY menu and a true start game function.

Also, redesign all the map that they are more fun/interesting, (objectively, in my opinion).

Temporaly make the camera fixed in the middle of the map, instead of following the player.

Happy International Woman's day <3

-----------------------
### Sat Mar 7 22:41:50 2020 +0200

### [2hr]The place object on top-left function works. Now, I will work on the main menu (maybe not needed), but definitely a restart function. And a buy menu. After that, the game is presentable/playable? Maybe?

-----------------------
### Sat Mar 7 00:34:38 2020 +0200

### [1.5hr]The map loading menu works. I also finally got a really nice looking logo from the guy on Fiverr, which, I'm quite satisfied.
Map loading works unloading old map and loading new map. Also retain the position of all objects on board. Still needs the automated position finding for object placed on non-ground tile but I guess I will work with that tomorrow.

Add a start menu scene, so I will try to make a start-menu next (tomorrow), so I can test the Restart function of the game properly.

-----------------------
### Fri Mar 6 00:11:09 2020 +0200

### [1hr]Remove the place-holder unity editor fields in the grid-manager to store the sprite data of each gridtype. They are now store properly inside a json file name GridTileData.json
Spend most of the time wondering why my json file also return an exception when tried to load. It turn out that your json file, while being read by the C# Serialier can not have extra comma \,\. For example, this is perfectly fine in js, or even typescript

{"a":"a-field", "b":"b-field",} -> The extra comma after "b" field is completely fine in js or ts (or even Python, I think), but will fuck up either the C# serializer or UnityJson parser real hard.

-----------------------
### Tue Mar 3 00:13:06 2020 +0200

### [1hr]Add 2 new maps (floor plan/maybe) so we have 3 maps total now. It's not needed, just fun thing to do. Add some ground works so that the loading of the map will be handle better.

Just watch the Oscar winning movie Parasite, it's good, I like it, genre mixing film with some underlying views of the system, nice movie.

-----------------------
### Sun Mar 1 23:40:20 2020 +0200

### [2hr-Working on the logo on Fiverr]-[1.5hr]Redraw the recycle bin sprite, it looks slightly better. Add a computer sprite, in which the customer can use to buy stuffs, like food/funiture to their kitchen.
Also, the guy from Fiverr already delivered his works. It looks lovely, now I really do regret that I didn't pay extra 10 dollar to have access to his source file. I asked some small revision (his logo looks like a noodle bowl, instead of Pho Bowl), and ask if I could pay extra to buy access to his source vector file.

-----------------------
### Sat Feb 29 23:52:39 2020 +0200

### [1hr]Add a quick fix to the Game Grid so that we can not place object on top of it anymore.
Next, will try to make a function that spawned object, if placed on a wall, will try to place it on the top left corner of the screen or some where similar.

-----------------------
### Sat Feb 29 15:19:12 2020 +0200

### [3hr]The UI Save/Load Layout is now functioning with 3 slots. Will make so that the map-load works properly next.
Try to solve the button selection bug but couldn't do it. I am thinking I should make it so that if nothing is selected, and a controller button is detected, it will automatically select a top UI button.

-----------------------
### Sat Feb 29 01:16:33 2020 +0200

### [3hr]A lot of struggling with the UI codes and now Doozy and Rewire finally works together for now, but it's quite a bit buggy for me.

How to make Doozy works with Rewire: This is quite a band-aid fix to the problem. Because I'm using 2 plug-ins that doesn't intended to work with each other: DoozyUI and Rewire. As far as I understand, the DoozyUI only allow "onClick" function to be, a mouse click or a touch/tap. Thus, button pressed using controller, will not be recognized by DoozyUI Button. That's because Rewire UI register to the EventManager, sub component of Unity UI, while DoozyUI handle button pressed on it owns, thus, ignore the Unity Event system (I think). Thus, the fix is really simple and band-aid. If the button register an on-click event, execute the Doozy Click function. This can be troublesome, as the ExecuteClick will be call twice if we click the button with the mouse, but I don't see any problem, so probably there are some under-the-hood code that check for duplication. Also, note here just for future reference because having an additional Component to every button is annoying. I just go straight into the DoozyButton code and register this listener myself. In their OnEnable and OnDisable fucntion. Also, quite funny that somehow after adding this "fix" the [B] button suddenly works as a back button.

Another bug with selection: There is this huge problem with the UI is that if the user CLICK the mouse outside of the Menu Area, all button will get deselected, thus, make us un-focus on the menu, thus, make it impossible to control the UI with the controller anymore! Need fix!

Also, there is this brief bug of if you are scrolling around the PauseViewMapLayout, if you press BACK while moving the cursor, the menu WILL lose selection base, and the only way to get out of that is to exit the whole state.

Mom have left this afternoon, go back to Vietnam, not live with me and my wife anymore. While it was sometimes irritating living with her in our relatively small apartment, now that she's gone, I do miss her.

-----------------------
### Mon Feb 24 23:44:00 2020 +0200

### [1hr]The pause menu works now. There is a nice NULL reference bug, going right after another pause logic bug of mine, that make the game fully functional, but I should fix both of them.

Like it's interesting, 2 wrongs make an smooth game. But I should fix it.

Also, got a new used apple watch series 3, so I'm just messing with it. Seem fun.

-----------------------
### Mon Feb 24 00:05:41 2020 +0200

### [2hr]Successfully import DoozyUI into the game. Doozy UI works as well as it's expected, but I still have a lot of questions.

Like I'm not sure the proper way to have a pause menu and then enter it at the press of a button. Like, hmm, how ... I'm doing work around and I feel like it's totally wrong.

The importing error is also weird, they have one error line, and if I remove that, it will install normally. But it didn't happen with my test project, which is like, err?

-----------------------
### Sun Feb 23 22:18:09 2020 +0200

### [15mins]Add proper PC keyboard map to the game, so that PC also have equivalent of Y and B button now. (V for [Y] and B for [B])

I though there is some bug caused by the recent map loader change that make picking up object buggy, turn out problem is that I was charging my mouse, which make my xbox controller un-plugged, so I had to use my keyboard, which make me realize that my keyboard mapping is incompleted.

-----------------------
### Sun Feb 23 22:08:02 2020 +0200

### [4h]Trying to learn DoozyUI again after I realize that I will waste a lot of useless time at the menu stuffs.

I think I learn enough of Doozy UI to use now, it's a really amazing asset, the only problem now is that I just can't import it to the current project, which is a huge annoyance. Anyway, update DoTween because I though it would help (but it didn't). Commit to save the upgraded DoTween version, will try more.

-----------------------
### Fri Feb 21 00:07:30 2020 +0200

### [1hr]More working with the Save load ui. Mostly just experiment with Button.onClick.AddListener(function with param).

Encounter a really weird issue, where I can't use the i index of the loop directly, if I do so, all the function will be called with the max index. Which is weird.

Here is the problem I'm talking about

```
for (int i =0; i < buttonNums; i ++) {
    buttonNums[i].onClick.AddListener(() => { myFunction(i)});
}
```
If I use this, all the button, on click, will call myFunction(buttonNums), not myFunction(0/1/2) as I would like to, so I have to make a

```
int index = i, and use that index value. Which is weird .....
```

Also, UI is quite complicated, so I might looking into reinstall Doozy UI again if it save some times.

-----------------------
### Thu Feb 20 00:28:50 2020 +0200

### [30min]Start working on a save/load layout menu so that we can have multiple save layout as well as save slots. Let's go with 3 for now.

Tried to do more, but ended up getting in the rabid hole of youtube. I have been playing Hitman 2 recently, Hitman Blood money still is one of my favorite video game so I really like hitman 2016. Haven't actually play the new map in the hitman 2, just played all the map from the first game, but ported to the second game, and I love every one of it so far. Kind of rush through each level and only run once, no replay, but still really nice game to play.

-----------------------
### Wed Feb 19 00:07:36 2020 +0200

### [1.5hr]Map a map editor/map loader of sort. It works, but needs a lot of bug fix.

The map is just a text file of x * y dimension, with proper error handling of course, with text making each type, for example, w is WALL, k is KITCHEN. It works now, but I think lots of extra work with the GridManager. Mostly because coordination is a difficult stuff, and I don't want to change already working code too much.

Example of a map:

```
wwwwwwwwwwwww
wyyykkkkkkkkw
wyyykkkkkkkkw
wyyykkkkkkkkw
wyyykkkkkkkkw
wyyywooooooow
wyyywooooooow
wyyywooooooow
wrrrwooooooow
wrrrwooooooow
wrrrwooooooow
wwwwwwwwwwwww
```

-----------------------
### Thu Feb 13 00:47:08 2020 +0200

### [3hr]Prepare the steam page again.
Previous time, I got declined because I didn't have a logo, so I, with the help of the wife, make an okeish logo, prepare the steam page again and upload it. Took a lot of time.

-----------------------
### Tue Feb 11 23:44:41 2020 +0200

### [1.5hr]Making 2 new gif for the website.
Learning the tool mmfpeg, really nice command line tool for making gif, but there are a lot of annoying display artifact, which make the gif look a bit noisy. Also, try installing ubuntu and linux for window, because the bash script I need to run the file is a .sh file, but well, it doesn't work. So ...

-----------------------
### Tue Feb 11 00:40:08 2020 +0200

### [5hr]Work my ass off to update the websites, update the git commit, generate game play clip.

The game play clip was created using Davinci Resolve, which is a really decent free video editor software. Really nice, some small hurdle at first, but it works out nicely.

I didn't even have time to create some gif and graphics, just a screen shot of the game and the teaser trailer. But I guess it's nice I guess. Maybe I should try to setup the steam page soon.

The commit on this project is just a spiritual one because all I did was remove one line. Most of the works were done somewhere else, but I want to log it here anyway, because I want this git-log to be the main source of dev-documents.

