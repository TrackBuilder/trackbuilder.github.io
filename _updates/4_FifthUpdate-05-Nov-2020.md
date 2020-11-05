---
post_time: "5th Nov 2020:"
title: "Fifth update. 3D change and baby boy!"
excerpt: "2020-11-05 - Progress update"
toc: true
layout: posts
feature_image_path: "/assets/2020-11-05/serving.gif"
---

+ Ok, the change to 3d takes longer than I though, 2 months for this update instead of well, I originally thought it would take 1 months only, where I know that if I work super focus, it should take 1 week.

+ Still, I welcome a new member to my little family: my baby boy. He was born on 24th Oct 2020, 3.75kg and 50cm, and stayed in his mom's belly for 42 weeks and 1 day. He came out healthy and has been a very good boy for us.

+ For the change to 3d, because most of the logic and calculation was done using my custom-made grid system, it's actually fairly simple to change, just need to revert the Y axis (in 2d) to the Z axis in 3d, and let the Y axis as height. There are some complication with sprite and lots of 3d models import and asset creation, but it's not a too difficult task.

+ The most difficult task is now to make the game beautiful. Right now, the game looks like an early PS2 era game, which I have some idea on how to make it looks better, like cell-shading and some cooler effect.

+ Probably plan to refactor the whole food-recipe creation. I made it with the idea of using it as both food-data, as well as sprite look up data. Now that I don't use sprite anymore (mostly) maybe I should change because if I just keep it as is right now, it's a big mess. Still, making the game looks nicer and controlling nicer is a priority first.

+ Some unrelated progress as well: seems like I found a new gaming addiction: Genshin Impact and gacha gaming. I know that gacha game is essentially you "gamble" for a png, but well, at least in Genshin impact, it's a whole 3d model with customer rig, animation and really nice gameplay. I have dropped (5.5e x 2) (monthly gem bonus) + 11e (battle pass) + 55e (gem pack) + 18e (gem pack) on this game, but I feel it worth it. Today, I almost bought another 33euro pack, but decided against it as I could buy a full game with it (like FireEmblem 3 houses or Disco Elysium), but then I didn't buy anything either because if I bought it for switch, or PC, I will just play like 5 hours of it, and feel regret, or worse, spend 100 hours playing them, which is also bad. So maybe spending money on this game isn't that bad?

+ Anyway, progression.

![image.png](/assets/2020-11-05/organize.gif)

+ Cooking!

![image_2.png](/assets/2020-11-05/cooking.gif)

+ Serving the customer.

![image_3.png](/assets/2020-11-05/serving.gif)

-----------------------
-----------------------
### Fri Nov 6 00:24:49 2020 +0200



### [2.5hr]Update the processor component, and tweak the camera angle. The 3d transition is now officially done. Also, write the progress update.



-----------------------
### Thu Oct 22 23:36:17 2020 +0300



### [1hr]The game is now fully working as similar as the 2d version now. So now I can just start to add cool shader and refine the movement.


+ Fix the problem with progress bar, like somehow the progress part is sometimes behind the background. At first, I was doing really dummy way of setting the position to like -0.01 for the main part and 0 to the background, which might cause the issue. The proper way would be to change the order in layer, which I fortunately know from doing 2d. So doing this in 2d isn't a total loss of time at all. Also fix more positioning bug with the progress bar like icon was at -2 pos so it's so far away.


+ Each food container now have a small text on top of it saying what ingredient it currently have, or in case of finished, what recipe it is. Because now, you can't tell which food container is which, and also, adding my old sprite to the popup would take too much refactor, which I plan to demolish the whole game recipe anyway. I did it initially because of 2d and sprite loading. Now I have 3d and none sprite loading, so I should do it in a less confusing way.


+ The dining table has been update to be the same, so that if a customer is requesting some food, it will display the name of that dish.


+ Remove most of the tween animation on 2d object, it's just weird.


+ Right now, the movement is really akward, I think I need to fix it somehow, by resizing the object so movement is a bit easier, and generally, just placement of 3d objects.


+ My son is expected to be born tomorrow, I have no idea when he will actually born, but exciting time ahead, and probably, busy time as well.


+ I have been spending the last 8 days playing mostly JUST genshin impact, after spending soo much money on it (so 55 for the guarantee Venti pull, and AFTER that, I got greedy and spend another 17 euro to get 10 pulls to get more dupes of 4 stars so they get stronger, pretty good pulls though as I was able to get 1 fish and 2 barbaras). And 5 euro on a monthly gems (for a month, their value equal paying like 35euro) and the battle pass. Eventhough I spent a lot of money on that game (like 3-4 times I would normally on a normal game). I don't feel regret spending on that though, because somehow, I know exactly what I get into, and yeah, I just like the game that much. I also might have problem with Anime girls and gambling problem though, or at least, buying impulse.



-----------------------
### Wed Oct 14 00:09:10 2020 +0300



### [1hr30min]So, the food-container updates its model properly now when there are food added and when completed.


+ The whole recipe data I wrote a while ago was for the 2d sprite, which is a bit confusing. With this change, I could delete a lot of data/code to make this looks a bit clearer.


+ Right now, when ingredient is added to food container, we have just one generic model for that, which make things super confusing, because adding vegetable or beef or chicken or anything to the bowl shows nothing different at all. This probably need to be fixed, to either have their little icon shows over the top like in Overcooked and DinerBros.


+ Fix a bug with Tofu sometimes not able to drop it down. Turn out because I didn't remove the box collider from the model. Nothing big.


+ See a bug with the progress bar component will fade behind the background (so it looks greyed out). It happens until the bar reach like 50%. Will investigate more.


+ Also, if an object has progress bar popup, and we move it around, the progress bar is rotated as well. We should make that thing a bill-board shader, always facing main camera.


+ When cooking pot is finished cooking and has its content taking by a bowl, its Z scale is set to 0. Will fix.


+ Overall, my crappy pumping animation 2d doesn't looks that exiciting in 3d. Will need to fix later.


+ Right now, I think it's more important to just make everything works again, so next I should make customer and food order work. After that, is the clean-up phase, which will remove all the 2d artifacts and makes it more 3d friendly.


+ I played a lot of genshin impact today, but actually, just mostly reroll account (3 times only, not much though). Basically, somehow in the morning I have the briliant idea that I should pay 55 euro on this game, so that I will get the limited banner character (Venti). He's super good, S rank, and it's nice that this game have a pity system so that you are guarantee to have your star characters, so you will never spend too much. (Well, if you have ultra bad luck then you need like 200 to pulls the banner characters, but it's not much compare to other gacha games. Not that it's a small amount though).


+ So I have been going over it a lot, basically, it not worth it, but because I am soo commited to this game, and this character is a limitted one, which means he probably won't come back until next year, so now is the only chance of getting him. And if I drop money to pull him, I will also have another cool character as well so not a 100% loss.


+ Which makes me think of how Gacha game really works. They aren't straight forward P2W, actually, most of the content can be clear with just normal guys, what they did is they create a really fun game, and requires you to play a lots. And then, they show you just a little bit of these really cool and awesome character (that's also very cute). You can absolutely play fine without that cool character, but your gaming experience will be much better with that character, so yeah, get you commited to it, give you free gems so you can try, and only then, if you are really hooked, you will pay good money to pay.


+ So, I tried reroll for that character (Venti) (means I create new account again, which they give a few gacha for free, so people reroll until their first chars are what they wants) which I did successfully. But then comes the problem that the character on my main account are actually way better, just that it will be even better with that Venti, which means I need to reroll to have 2 5* on my account, which basically means impossible.


+ Yeah, like, really addicting thing, let see how this pan out. Like, I can dish out 55euro for this game, but I feel that these kind of money can be much better spend else where, like 1 week worth of food, or a new shoes, lol. But we shall see, the guy is on gacha for 4 more days, I will try to farm gems until 1 day left, and then let see if I will pay money, (and how much)



-----------------------
### Mon Oct 12 23:28:39 2020 +0300



### [1hr]Ingredient now loads the correct models when finish processed. Change the collider of all prefabs from sphere to box.


+ The ingredients now load their models correctly. Next I will try to make the food container models update correctly as well as fix bugs that I have with them, like somehow the processor component doesn't show up.


+ The object's prefabs are changed from sphere to box. The player now doesn't stuck between object now, but moving around corner is a bit slugish. Need quite a while to fix though.


+ Seems like all the object in the game (table) need to be lower, like only to be 0.5 or 0.7 of the x and z size. I was keeping everything in a 1-1-1 dimension box but seems like too high object make things clipping quite a lot and also asthestically not nice.


+ Doesn't help that the game looks totally ugly due to the everything is still in the default model, definitely will buy some cool anime shader soon.


+ I feel that if I do sit down for like one full day and work, all of this will be complete, but I just keep doing something else, and not even talk about playing game. I finished eating at 7.30 today, and now is 11.20, but I only dev-ed 1 hour, I just keep doing stupid thing, first, just aimlessly watching TV while waiting for my 2 roomates to finish sauna so I can do my sauna turn. After that, I was free from 9.30 but somehow just get distracted by the stupid reality tv shows on the tv right behind me, and then 10.15, walked the dog for half an hour. And dev a little bit until now. So that's a 1 hour dev in a 4 hour span. I mean, if I can play games for 2 hours, walk-dog 30min, and sauna + shower for 30 mins, it's much better time spend than that, which I waste 2 hours for something I don't even enjoy.


+ Talk about game, I was playing Genshin Impact all day Sunday. I logged on in the noon and decied that I want to do some side quest, which then I found a stack of 3 Wind-culus, sort of collectibles in Genshin Impact that help increase your character stamina. THen I thought that if I found a big stack already, it's helpful that I will collect them all so I won't be distacted by them again, and in the future, I will want to collect all anyway, so doing now will be better. Spend the whole day (afternoon and evening) just to hunt down these things (using online interactive map) and still miss like 3 out of 65 of them. These doesn't show up on your world map, only shows up in minimap when you get close, and I have been going twice over the whole map, so I have no fucking idea where these are. So I officially give up on these until they release a patch that is more finding friendly. Yeah, still, I found these mroe fun/enjoyable than watching stupid (informative) youtube and reality tv shows.



-----------------------
### Sat Oct 10 23:59:56 2020 +0300



### [0.5hr]Fix the progress bar bug found yesterday. It was the bug with progress bar, not the 3d prefab.


+ The game movement is now a bit laggy and slugish, because every object is a sphere collider, which make player easy to just stuck in the middle, which make movement weird. Easy fix would be ofcourse just make them box collider, but then it's easy for the player to just stuck at the corner. I currently can't think of an easy way to fix it. The hard way would be to make object that is next to each other will have box collider to prevent player from falling in, and normally will be sphere collider. Will take a lot of time for detecting these thing though, which is not really optimal.


+ Didn't work much today because I just coded a little bit in the morning before lunch, after that, driving for the food supply, and just chill with friends for the rest of the night. Also a bit of playing Genshin Impact. It's crazy, they gross over 100 millions after less than 2 weeks release. With a budget of total 100m (including marketting).


+ I read a lot of critism for the game for being too expensive to buy, but I think you need to approach it with the patient mindset. Like, just pay the 5.5 euro pack that give you small amount of gem everyday (like I bought today) and just play little by little everyday). Rushing is only viable for big spender, normal people just play patiently. People bash the gacha, ofcourse, but I think it's what make it fun, playing with luck, and don't know what to expect is fun and interesting.


+ The game progression feels really good as well. In normal RPG game like Witcher 3, Assassin creed, because it's purely single player game, then exploring and "farming" feel super useless because the game makes you so powerful already, so no need for farming anyway. In this game, exploring and farming is fun because it helps making you forward the goal of being stronger because end-game content is really hard.


+ Ofcourse, there is a lot of "bad" grinding single player game as well, that why I say this game make farming soo rewarding, which make it really nice.


+ Ok, off to play game now, will try to work more tomorrow.



-----------------------
### Sat Oct 10 01:00:20 2020 +0300



### [1.5hr]So, the pick drop component works now, seems to be able to even chop/process object. Also fix the player height a bit.


+ The pick drop actually works already, just because of some forget-to-code part that doesn't update the object to proper table position when dropped on table.


+ Can chop food on the cooking board, but the process bar component position seems wrong, and it doesn't update the model when completed (yet)


+ Fix the player height and the picker position. Now I see the problem that the current player asset height doesn't match super well with the restaurant models. Also, the color looks super dulls so I need to use some cool anime shader next (I guess).


+ Has been super addicted to Genshin Impact. In term of enjoyable, I enjoy it the same level as BotW, more than Witcher. Such an incredible world just to get lost in. Only problem is the gacha, but I have been bless by the RnGesus with a really cool 5* character (Keqing) which has been super fun to play. Read a lot of valid critics on reddit about the game though: gated progression, un-generous gacha rate (0.6% for 5*) and really lackings free to player reward (like, 10 pulls for 1 month of play?). Still, I'm low level compared to the current max (21 mine compare to 29 which is the point the game runs out of contents). So the game still have a lot of magic and awe for me. Will probably stop play or just log in 20mins per day for dailys  and shit.


+ Still it's such a miracle of a game that you can play serious on PC, and play a bit more casually on the bed before going to bed. Like, really cool about that.



-----------------------
### Thu Oct 8 00:56:11 2020 +0300



### [2hr]Create the ingredient models for the ingredient I have in this game. Also, I can grab stuff from the container now, just can't drop them.


+ Well, for ingredient models, I don't create them, just use premade one, and you know, like few hundreds of models, just choose which one is correct for my game, and some slight resize, re-adjust position, and sometime merge multi models into one. Cost a lot of time though.


+ Update the ingredient object data as well.


+ The ingredient data model works the first try, so I'm really impressed with my code system, as I though it would require lot of change. Just remove one Collider2D component call from code and it's done, cool.


+ Monday, I added the PrefabCaching, with the intention of only using it for loading model for the food container, and wow, suprised today, I need to use it for the ingredient object too. My code was quite modular already so nothing big is needed to changed, just a bit wondering why I didn't think that I would need it for the ingredient. I guess I was tunnel visioned for the food-container only.


+ Been sucked to playing this game called Genshin Impact, a Free to play Chinese gacha game. It's quite fun, and even if you don't pay, the game play is super good, not as good as BoTW as many people claim, but close and fix some minor annoyance with that game. Gacha game is quite fun, maybe the next game I will try to add gacha mechanic into it, but with 0 microtransaction (whale hunting) because it's really evil. But yeah, playing with your RNGesus is quite fun as the out-come is un-expected, the super cutie waifus help that significantly as well.



-----------------------
### Mon Oct 5 00:48:01 2020 +0300



### [3hr]Fix the loading sequence, at least the game loads now and everything looks normal. All models load correctly. Next will finally rework on the object inreaction.


+ Fix the ingredient spawner. so that now it will have the spawned ingredient type as a sprite renderer sprayed on its side.


+ The Food Container (Bowl, Pot) both have their own model now. They still works the same way as previously, as they are the same prefab, just different config ie: sprite and some setup, but previously, I can change the shape just by changing the sprite, now, I need to load a new GameObject in the Resouce folder can't load Just the mesh because different prefab have different materials, beside, some Object even have some children object for decoration.


+ So, to continue the above, the data file now has the path to the prefab object, and each food container has a Dictionary, so that if it loads a new form (Bowl of Pho,  Empty Bowl, Dirty Bowl) it will load the object and store in a dictionary. And if that form is called again, it just re-active the old one and all other are de-active. This save a lot of load time with the expense of few more objects.


+ Huge delay because I have been playing Hades (and some procrastination) a lot. Actually beat the game and unlock true ending. I like the game, but it's not fair to say it's a rogue-like, because everything you have is a progression, like, you really can't beat High-heat (skulls) without tons of titan-blood upgrade, and well, the game feels a bit too same-y after beating it a few times, unlike say DeadCells or Slay-The-Spire. Also, post-game contents (1->4BC in DeadCells or Ascension climbing in StS) feels weak. Just the same game without the wow effect.


+ Still, base game is amazing and I enjoy a lot of the time I was climbing the rank and trying to beat Hades. It's a hard game for sure, but I think the hardest part is just to know which boon/bonus to pick, not the actual difficulty of the game. If you know what boons/power-up to use, the game can be dead-simple sometimes. So yeah, the game is more about game knowledge, rather than player skill, but it initially gave me the impression of inverse.


+ Also, have like 2-3 nights of not touching the computer. One was because of my birthday party (which some guy rear-ended me) and other was because of a board game night. But yeah, this 10 days away was bad :(



-----------------------
### Thu Sep 24 00:29:48 2020 +0300



### [2hr]Add the foods and furnitures models to the game. Update the prefabs with all new models.


+ Game looks passable now, lots of null error open creating game, but player can still move around and game looks 3d-ish now.


+ Default unity shader/lightning doesn't work really well with low poly model, it looks like some low budget ps2 games. Still, it's progress as we are slowly approaching 3d nows. Feels good to be able to delete a lot of files and still maintain the same game.


+ Simple furniture works now, but complicated case like FoodContainer/ingredient/ingredient spawner doesn't work yet because they have dynamic sprite. Will think of new ways for them to work next.


+ Acidentally drag the Doozy folder (UI libs) to the resource folder, which cost like 15 minutes of re-importing assets, and then move them back again cost another 15 mins of just waiting, there should be some-way in unity to lock folder so you can't move them anymore. Even now, the Doozy folder update some assets for some reason, so I'm going to just commit them because the change seem harmless.


+ Rocket League gone free on Epic store today, and if you claim it, they give you a 10euro voucher (yay), which I take and use on Hades. Been super pumped to play the game as I discovered it yesterday, but then making this game takes the whole night. So I can't play it. Super sad :(


+ Now that I learn about marketting, it's not enough to let people hear about your game, you have to let them hear about it multiple times. Yesterday was like the 4th time I heard about Hades? few from reddit news, few from Steam and once from my co-workers say how it's an excellent game. I only was interested in it because I learnt it was a Rouge-like.


+ It's funny that I have been wanting to play MoonLighter, which I have for free from the Epic Store for soo long, but haven't even downloaded it, but the moment I know about Hades Rouge-like (and watch a youtube vid about it), I was super pumped and so ready to pay for it. To sell a game, you need an excellent hook.



-----------------------
### Wed Sep 23 22:48:10 2020 +0300



### [2hr]Remove the old zDepthSorter. The player pickup highlight now works. Commit so that I will import some food/kitchenware in the next commit.


+ I mostly remove the zDepthSorter because all the 2d component rely on it, so if I remove it, and clean until there are no compile error left, it's probably complete and safe to move forward


+ Also, remove some directional function I made to determine the direction of the player. Now, it's just simple Y rotation only, which make things a lot simpler.


+ Some fix here and there with the 3d renderer, commit mostly so that this commit won't become too big, because I will import lots of food and funiture to the next commit.



-----------------------
### Wed Sep 23 00:29:28 2020 +0300



### [2hr]Finish with the grid-map-tile. Make shadow works, start changing all the prefab to 3d.


+ The grid-map now is a 3d plane, with textures, instead of sprite renderer. Wall is a cube and is higher, so it is actually a 3d object.


+ The player and object now can cast shadows, and the plane can receive shadows as well, it didn't work at first, turn out because the project setting was set to 2d, which disable all nice 3d features. I think I will need to convert this project to URP for performance gain and nicer 3d graphic (Universal rendering pipeline Unity)


+ Start adding 3d object with some textures to all the game prefabs as the ground work.


+ Will update the player controller code, so that the picker and holder object will also have a 360 degree ranges. This means I can delete a lot of code :p



-----------------------
### Tue Sep 22 00:47:39 2020 +0300



### [1.5hr]Make the 3d character animation. Also, prepare the ground tile to be proper 3d model.


+ Right now, the ground tile are 2d sprite renderer, I want to make them 3d plane with assignable texture, so that they can receive shadow, cast from the player.


+ Maybe proper wall object? Lol


+ Move some files around. 3d models folder rename and such.



-----------------------
### Mon Sep 21 00:27:00 2020 +0300



### [30min]Buy the 3d humanoid models, import to the game, add light to the scene and fix a movement bug I made yesterday.


+ It's technically tomorrow from the last commit, because I commit at mid-night, and now, this commit is at 00:26, so I really buy and import the model the next day.



-----------------------
### Mon Sep 21 00:00:08 2020 +0300



### [15min]Remove git-ignore for all my purchased assets so this project can work as-is, as in, just clone and work, no installation needed.


+ As this is a private repo, and I'm working alone, so I'm not distributing these to anywhere. So now, I'm using a old version of Unity with old version of the assets, if I would use a new computer, then it will be big problem, compile error when I clone this project.


+ Also, buy a humanoid asset to import to the project. Just buy, import will be done tomorrow.



-----------------------
### Sun Sep 20 00:44:34 2020 +0300



### [1.5hr]Add the 3d model some 3d rendering code to the player. It can move around with the player and face the direction it's moving now.


+ The 3d model is now in a T pose, but at least it face the direction the joy-stick is pushed to now. I think this only would make targetting/picking/dropping stuff much more responsive and more natural already, as the previous system only account for 4 directions stuffs picking, which I think isn't good enough, and feels quite limited. Now, it's full 360 direction, so probably feels better.


+ Small refactor, as move the GetComponentAndNullCheck from BaseObject class to the static utils class so all the GetComponent and Null check is at the same place.


+ Wasn't planning to code anything today as the family went for a small trip to Porvoo, but then I have some spare time and decided that maybe I could do a little, and funny thing, something produtive, so yay me!.



-----------------------
### Fri Sep 18 00:41:25 2020 +0300



### [2hr]Finish with the gird-coordination change from 2d to 3d. Also, player movement works now (again). Tomorrow will be pick/drop functionality.


+ Seems like most of the Grid map, placing and validation works now. My map is spawned just like before (on screen). My code is quite modular so I mostly need to go to the grid manager and map manager class and change from y to z.


+ Ofcourse, this being a top-down game, so moving to 3d is more of a art-direction change rather than like, game design decision that I need the extra dimension or though.


+ Now that I wrote that down, I could have gotten away with just keeping everything the same, but use 3d models/camera, renderer but with the same 2d logic. But that would probably hurt more in the future, and my harm some lightning or something. Anyway, if I decied to do 3d, I should do 3d properly.


+ Remove all the 2d Collider from prefabs and change them with box collider 2d. The player movement is also updated from rigidbody2d to rigidbody 3d, it works almost instantly, as I only need to change a vector 2 (x, y) from the controller input, to a movement velocity of (x, 0, z). So, really small change.


+ Tomorrow, will try to make the pick/drop thing works again, so it means thing will be back to just before, minus some sorting/layering issue, but then, we are going to remove all the sprite anyway to change them with 3d model, so whatever.


+ Will probably not work tomorrow due to a birthday party. It's not like I work so continuously and I sometimes (usually) just skip one or few days of developing game just because of game/watching movie/distraction anyway.



-----------------------
### Thu Sep 17 00:31:39 2020 +0300



### [2hr]Starting to add 3d to the game. First step is to redo the map grid system.


+ Because unity3d use xz for ground position, and Y for height, while our 2d top-down game use X for horizontal and Y for vertical, so everything, in the view of a 3d camera proper-view just are from the top down.


+ To fix this, I will just try to go to every part of our code, mostly the grid and map system, to change Y position to Z position. Success would be that I am able to see the map like before, but with 3d camera view from top.


+ Next would be harder, which is to change all our 2d physics (2d rigid-body, 2d collider) into 3d physics (character controller, 3d rigidbody/collider). After this step, our player should be able to move like normal, and actually playing the game just like before, just with 3d physics calculation instead of 2d physics.


+ Last step would be to change the rendering from 2d to 3d, which change all sprite renderer to MESH renderer with texture and stuff. Ofcouse, add light as well.


+ Hopeful thinking, this take a week if I work full time and really concentrate, but I don't work fulltime and I get distraction a lot so maybe like 1 month. Hopefully not that long though.



-----------------------
### Wed Sep 16 00:28:09 2020 +0300



### [2hr]Update the steam page to have the Progress updates. Import a 3d humanoid model to start with.


+ I initially wanted to have each update as an announcement/post/event, like games like DeadCells/Noita,... have, like update 19, 20, things like that. But seems like it's not possible with an un-released game.


+ Stared at the project for a while without knowing where to start. Hmmm, this is like a huge task.


