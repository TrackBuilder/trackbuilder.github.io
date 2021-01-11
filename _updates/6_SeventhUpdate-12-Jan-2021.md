---
post_time: "12th Jan 2021:"
title: "Seventh update. Happy new year. Calendar system, baseline NPC and lots of UIs improvement!"
excerpt: "2021-01-12 - Progress update"
toc: true
layout: posts
feature_image_path: "/assets/2021-01-12/calendar.gif"
---

+ So, happy new year everyone! I played Persona 5 and I just loved the calendar system there, so I implemented a calendar system into the game. It should work well thematically and in a meta game, because running a restaurant is half the work you do at the restaurant, and the other half is the planning, logistic and everything.

+ Decided to add some NPC judge to the game as well. Right now, they are just standing in one place, but hopefully next update, I will be able to make them walk around a bit, and have atual customer animation that move around, not just spawn. And hopefully, a queue of customer right at your door.

+ I have some kind of random event system in mind, like things that you can do in the MORNING or EVENING (because AFTERNOON is for running your restaurant), right now, just money boost but I will try to add more. Something like going to class to make you cook better food.

+ Yeah, I want to make the food has level, so you natually progress better, like at the start of the game, your food is like 1 star quality, and by the end, your food would be like five stars or ten stars, and you have to improve your food quality by having better ingredient, have better cooking techniques, have better equipments ... All these must be gained via game event (like going to class or something), or buying with money.

+ Yeah, some progress, nothing new in gameplay or graphic because I mostly did UI change.

![image.png](/assets/2021-01-12/restaurant.gif)

+ Serving and multitasking!

![image_2.png](/assets/2021-01-12/calendar.gif)

+ Some organizing at the restaurant.

![image_3.png](/assets/2021-01-12/open_restaurant.gif)

-----------------------
-----------------------
### Tue Jan 12 01:21:07 2021 +0200



### [3hr]Add tutorials, remove some temporal cheats AND udpate the website (create a progress update).


+ Deadline is tomorrow and I spent like 2 hours watching youtube videos with my wife about Japanese life. Time well-spent though.


+ Well, today, I completed with the code and progress update, tomorrow I will create the video. I will probably have enough time, hopefully.



-----------------------
### Mon Jan 11 00:42:24 2021 +0200



### [2hr]So, now we have 3 npcs as Judge, Seller and Event. I'm done for the demo, so tomorrow, I will play the game to get gameplay video and then edit a clip to add text on top of that to explain what I want.


+ One to open restaurant, one to sell normal item, and one to generate Event. As for event, now, I can only think of a special deal to buy hard to buy item, like food processor or dishwasher. In the future, the event should be like small quest for the player to do, so that they can get strong items or bonus.


+ Remove main UI map selection and player selection because the other 2 maps don't work, as well as the 2 players option.



-----------------------
### Sun Jan 10 20:28:56 2021 +0200



### [2hr]Add NPC class, which inherit from interactable object, and is world object.


+ A bit akwark but will fix later, after the demo deadline submission.


+ Make HUD works again, but now it will only display the money information.


+ So now, i have one evening, and 2 days left, to make it to the submission, and I have to make a video as well. So I will probably try to wrap everything today, and make the video tomorrow. Deadline is end of Tuesday (today is Sunday) but I don't want to wait everything until deadline, one day before dedline is ok though, lol.



-----------------------
### Sun Jan 10 00:59:24 2021 +0200



### [2hr]Add a confirm/define panel so that the player can response to random event.


+ For example: the player choses the option of rest and chill. So he watches tv at night. Then, he see and ads for the great Dish-washer, cost only 200 money. So he will choose if he wants to buy it, or not.


+ For option that doesn't requite any input, like just go to night-job and get 100 money (this option should be probably removed as well), then this show only one button, saying OK, and on click, will advance the time.



-----------------------
### Thu Jan 7 00:41:09 2021 +0200



### [2hr]Fix a lots of bug related to the fullscreen announcement and mostly pause/un-pause game issue and some callback problem. It's fully functional now so I can move on to another thing.


+ Working with UI is, well, just messy, so it's quite head-ache. Still I don't think this is the good time to beautify it because UI will just be changed/update/redo a lots of time anyway, so I will just use it as a bare minimum and just let the game evolve itself.


+ There is this event from IGDA Helsinki, that they ask people to submit their games and gameplay videos to them, they will pick 5 games, and play and just discuss it on their stream, which I think is a good chance for me to get feedback on my game, so that's why my commit frequency is well, a bit more than usual. But still, I don't think I can make a fully functioning prototype/proof of concept to them, so I will just make the best of what I can, and then, make a video and add lots of subtitiles on what I want to do and what not.


+ Deadline is 12th January, which is in just 5-6 days, so time is tight. And I have a fulltime job, and a 2.5 months old baby, so, yeah, it's going to be difficult. But on the bright side, AFTER the deadline, Ganyu (from Genshin Impact) will be released, and I have enough gems to purchase her, which is awesome. She will be the rewards for my hard working (lol) weeks.



-----------------------
### Tue Jan 5 00:31:35 2021 +0200



### [2hr]Kind of finish with the Game Choice selection UI flow, and have a pretty clear the flow of the UI/Game choice selection.


+ Now, I'm doing the fullscreen text pop-up, to make the game clearer to the player. It works halfway. Like, half the time, will fix tomorrow.


+ Time flow of the game:


* Start at: Week 0 - MONDAY - MORNING


* Enter-time/Advance-Time -> Choose option -> Update to UI Calendar, which is a list showing the player choice history, and if possible, all upcoming schedules.


* -> If options skip the night (rest/do night job, basically, just UI event that increase some stats, not asking the player to player the core game)


* -> Advance time again


* -> Show Calendar again.


* There are 2 souces of possible time advance. Either :


* 1. From playing the game (In-game events): Open restaurant / Restaurant close


* 2. Player choices (Ui-event): Go to sleeps, go to action


* The second kind will always contain some special UI scene, and then after that, show the calendar again.



-----------------------
### Mon Jan 4 00:52:15 2021 +0200



### [1.5hr]Test the game a bit and fix bug so that it works fully from start to finnish.


+ There is no "real finnish" though, so it just run, there will be a check (at the end of first week, for the demo) that say congrats you win and end it.


+ Add the day-of-week ui panel, to display what have the player been done so far, and any possible future events.


+ Move the config files around a bit.



-----------------------
### Sun Jan 3 22:41:23 2021 +0200



### [1.5hr]The game summary works with other UI now. I think. Will test more later.


+ Add the fullscreen announcement, to show like, new days and stuffs, acts like an transition scene, for 2second for the player to have time to understand what happens. It's there but not implemented yet.


+ Will test the Game Summary more. Also, the game summary ui looks ugly, so need adjustment as well.



-----------------------
### Sun Jan 3 14:37:11 2021 +0200



### [1.5hr]Add the fullscreen summary UI. The basic is there, but it is not chained to other UI element, just yet.


+ It used to be just the summary screen after you finish the day, show you the score, the money you earn, but now it should shows you every time before you open the calendar, to guide the player what should they do.


+ I want to add another Tutorial UI as well. Let's see.



-----------------------
### Sun Jan 3 00:45:32 2021 +0200



### [2hr]The restaurant phase is still keeped there, but adjust the HUD a bit so it display day/time information. Next, rework the day-summary, full screen fade-in-out notice.


+ The HUD doesn't have score/money information anymore, it's there but doesn't work, will rework again.


+ In order to make the game and the choice interesting, I will need to make the food and recipe has level/power, and more player skill means better food, this will require huge update to the food function, which is already quite messy.



-----------------------
### Sat Jan 2 15:06:45 2021 +0200



### [1hr]Finish with the ChoiceButton - choice manager button logic wiring. The problem now is rework the Restaurant manager.


+ Previously, the game has 4 phase each day: Prepare/Openning/Closing/Close. And most the game logic is depend on that.


+ But now, we have this time tracker and everything, the prepare phase can be removed. The Openning and closing phase can be keeped though. And the close phase, is just a check to tell it's the end of the Afternoon time and should show the calendar ui again to advance time.



-----------------------
### Sat Jan 2 01:08:20 2021 +0200



### [1hr]Not much, honestly, just finish the ButtonWrapper refactor, and completed with the choice button UI setup. Tomorrow, will work on the actual game logic.



-----------------------
### Fri Jan 1 01:35:05 2021 +0200



### [30min]New year commit. Make the button wrapper inherit directly from Unity button class.


+ I am trying to change every button instance in the game to button wrapper. I commited half way because I want to have a new commit in a new year, but it's like, half-way through.



-----------------------
### Thu Dec 31 01:18:06 2020 +0200



### [1hr]The Calendar ui now can get the data from the game choice manager and display the options properly.


+ Still, the hover text (when hover over the button) doesn't work (yet), because unity hides the state of the button (if it has been selected or not) quite deep under the button class, so I have to do some work-around. Maybe tomorrow I will just make my ButtonWrapper class inherit directly from the Unity Button class, sounds okei-ish.


+ Create base class for game choice button and day-of-week panel. Will also try to make some data class to handle the player selection and possible some extra state, like rest so that the player has bonus gains and bonus move-speed for example.



-----------------------
### Wed Dec 30 20:22:23 2020 +0200



### [1hr]Add game choice manager. Which is incharge of deciding what the player can and cannot do. Next, will hook it to the calendar UI and the game logic.



-----------------------
### Wed Dec 30 00:36:44 2020 +0200



### [1.5hr]CalendarUiController basic functionality (of the UI works), just needs to add game logic now.


+ So the button handler and how it reacts with other UI component, and how it flows into the game works now. I just need to update it so that there are logic in the game so that its button/data can get/send data from.


+ More functionalities added to the BaseUiComponent, to make things easier to work with. I mean, honestly, UI work is such an head-ache, because the UI can't be too easily capsulated. Like, most part it the game will requires update to some UI, so it's having one good manager to send data to UI become super cubersome, but on the other-hand, if you just make it too easy, then the code will become all over the place. A good way to do it is just make a lots of event/delegate and have the UI listen to these delegate, but then it's a bit too much of an over-engineering, as my game is just not THAT complicated yet.



-----------------------
### Mon Dec 28 22:56:35 2020 +0200



### [3hr][Sunday-code] remove new-rendering-component. Move GameDialog/DaySummary away from the head-up-display. More code to the CalenderUI.


+ The new rendering component was created when I was transforming to 3d, but seem slike there is something else in its place now so it's not needed.


+ The HUD had some popup info and day summary. I placed it there because I don't know where to put it, so it has its own canvas and controller class now.


+ Add buttons finder and function handler to the calendar, still the UI of the game still pretty much a mess now.


+ This was the yesterday code, but I stopped mid-way to take care of the baby and then spend the rest of the night playing Catherine Full Body. It has such an amazing stories and twists. Played from like 11 until 2 but it was good time spend because I was having good time, and not wasting time on reddit.



-----------------------
### Sun Dec 27 01:27:12 2020 +0200



### [1.5hr]Create a BaseUiController so that my current 3 ui classes (Pause, Sell/Buy, Calendar) inherit from that, because they have a lot of similarities.


+ Nothing much in term of progress, because I decided to spend 2 hours to wrote a small python script to check how much "worse" the permanent banner of Genshin Impact is compare to the limited banner, and then posted it to /r/genshin_impact and earn a total of 3 comments. Huge waste of time, but I guess it's a huge realization for me to not ever participate in reddit again. I have been using reddit for 6-7 years now and honestly, it's really pointless and such a time waster that I could have use the time on something far better, like actually playing the game instead of reading reddit.



-----------------------
### Sat Dec 26 01:27:26 2020 +0200



### [1.5hr]Add another confirmation UI for the calendar, so that if you choose an option, it will display detailed information of that activity.


+ Some ground work with the CalendarUiController.


+ I now kind of want to make all UI-controller inherrit from one base class, because all UIs controller has a lot of similar functionalities: such as a back button to go back to previous action/hide it, a background, and some functionalities to check state.


+ Also, I think a blur background UI would be nice, like a panel that anything pass through will be blurred, should be easy to archieve with either some shader work, or post process effect.



-----------------------
### Fri Dec 25 05:43:17 2020 +0200



### [1.5hr]Finish the design for the calender-view/day-choice option.


+ It looks passable, but the more important thing is I have something to based on, so I have a clear vision of what to do next.


+ I couldn't sleep due to many reason, so I decided to just wake up and did something positive. Woke up at 3 due to the baby (went to sleep after 2, lol) and then couldn't sleep for some reason, so at 4, I just come out here and did a bit of work, and also played a bit of Genshin Impact. It's good because I have been feeling really guilty for NOT working on the game, so working on this game and making some progress really ease my mind a lot.



-----------------------
### Mon Dec 21 22:21:28 2020 +0200



### [1.5hr]Refactor the JsonLoader a bit, so that the code is a lot shorter, and the look-up mechanism is the same as I implemented in GamePrefabDatabase, which is super nice.


+ Change the Dishwasher from object that can be dropped anywhere (on both table and ground) to be a Ground object, so that it can only be placed on the ground, AND you can place object on top of it, make more sense thematically.


+ Resize the Dishwasher a bit as well, so that it has the same size 1x1x1 square as other table object. Also, I think I want to add a small dish/bowl icon on top of it, so people know that it's the dish-washer, cuz now, it's a fridge.


+ The food container now, when received a completed dish, will change the text color from Yellow to Green, makes it more clear that it's a completed dish. Eventhough it was a place-holder feature, it works quite well for now I think.


+ I was planning to work with the GameActivities and stuffs, but got side tracked in fixxing bugs and improve the game a bit. Now, I will walk the dog. The baby is still awake now, but I think when I got back, if the baby is already asleep, maybe I should go sleep with him, because if not, it's 10.20 now, the baby will wake up at like 1. And then I have to play/feed him until 2/3 then, tomorrow, I will be super tired.


+ Because when we all go to sleep and turn all the light down, the baby sleep longer cuz he know it's night time. So, I also kind of need to schedule my sleeping hour around the baby.



-----------------------
### Mon Dec 21 01:04:03 2020 +0200



### [1hr]Start planning some classes for the Time-tracker/Game event system.


+ On Rogue-like game, you always have a sort of "stage"/long level to beat. For example, Hades, there are 4 worlds, Slay-the-spire: there are 3 acts and the last act to kill the heart. I want the game to also have a kind of 3 acts structure: 1st week, 2nd week and 3rd week, with probably big-boss/big-competition at the end of each week, and probably a short 4th week with the final really hard boss (like the Spire in Slay the spire).


+ Maybe make it so that you can "win" the game with completing the normal 3 weeks, but need to complete the 4th week to be able to ascend to the next level. Like, during each week, there will be special challenge that will be riskier, but you need to complete those in order to enter the secret round. (Like getting the 3 keys in Slay-the-spire)


+ I want to have a system similar to Persona 5 as well, where, for example: afternoon is mandatory, in which the restaurant is open. But you can freely choose what to do in the Morning and in the Evening. Like, you could choose to go to the restaurant in the morning to prepare the food, so you could probably meet the merchant there and buy stuffs, or maybe go to random event, like shopping malls, meeting friends, to gain special items or powerful or discount something.


+ We could make it so that you can decide to open the restaurant during the evening or not. Like, if you open during the evening, you will have more money, but it will be riskier, and your character will be super tired the next day, which reduce move-speed/cooking time/ something. Or, you can choose to go home early and rest, and gain bonus stats the next day. Or, choose to go out in the evening (also get tired too).


+ Still trying to think of a way to make the target of the game. For fighting game, it's simple, you kill all enemy and stay alive. But in here, defining your health is a bit problematic, and also, just trying to serve all the customer and reaching the target score is quite boring (like in overcook). I want something like, don't disappoint too many customer, don't let the customer hanging for too long, and maybe the Judge can give some super request like give them 10 processed beef or something like that.



-----------------------
### Sun Dec 20 00:48:21 2020 +0200



### [15min]Remove test code that make all FoodContainer dirty to test the DishWasher. Start adding a calender system.


+ I wanted to make it today but then baby was up the whole day and in the evening, my wife and flatmates wanna play some card-game so I join them. It was really fun though.



-----------------------
### Fri Dec 18 00:27:13 2020 +0200



### [2.5hr]Text config file is working now, with separate NormalConfig and CheatConfig that can be changed easily. Also small improvements and bug fixes.


+ Decided to use just .txt file because xml does mostly the same thing with json, which I don't need. Now, the system just load everything config into a Dictionary<string, string>, and get the config by KEY, and load the config using int parse, float parse or string to int array parse. Not the most performant way, but it's not going to be used much, so it's not a problem.


+ Now to think if it, if the whole config is in json, then the loading is very simple and no need for parsing as I can sepcify the field and type in the c# class and parse from json. The PLUS side of this system is that it's a bit easier to edit (since it's just one line of text: like, "StartingScore=0") and I can add comment freely. Also, I can have the lazy cheat config file, where I can JUST put in the field that I want to cheat, not ALL the field, where with the json, both files must have ALL the field, so tweaking values are harder. Maybe when the game is completed, I will switch to json config file for more performance, but I don't think it matters that much anyway.


+ The Dishwasher now have the small text display what it is doing, like: Cleaning Bowl -> Bowl CLEANED!.


+ The Processor bug about grabbing and spawning non-processable ingredient. I just disable that feature all together, because now that thinking about it, it's a bit too OP, like, if you have the food processor placed on top of a ingredient container, it becomes just GET processed food, whenever you want. The processor should only be able to skip the part where you don't have to stare at the chopping board for like 2-3s, that's all, not removing parts of the game. So yeah, bug fix by removing feature, justified by balance change.


+ Some data are still left-over from the game-data class. Might want to migrate them to the new config system too. But it's more dificult because they are State stored in Dictionary with my customs enums. Ehh, let's see.



-----------------------
### Wed Dec 16 00:34:08 2020 +0200



### [1.5hr]Rename the Recipe to English name. WIP the TEXT Config


+ The Text config is slightly more complicated than I though because config can be multiple format: int, string, array, heck, even I have an dictionary with enum there. Json isn't good because you need an equivalant class for that, which isn't idea. Right now, I'm using .txt file, but maybe xml file is the best?


+ There is still the bug that if you put the food processor on BanhPho, it will spawn an BanhPho in the middle of the map. That's because when putting the Food Processor on any container, it will try to grab objects from that container, which, in the current codebase, the act of grabbing will spawn the object. But, because BanhPho is non-process-able food, it will just dismiss it, thus, the banhPho is spawn in the middle of no-where. Because the Container class only have a function to check if it's possible to get from the container, but the food processor, GET from the container, and then check if the object can be processed, which is a bit tricky. Easiest way would be to just despawn the BanhPho if FoodProcessor does that, but then it kind of removes on BanhPho from the container, which will mess up with later game. I think I will need to add extra code in the food processor to check.



-----------------------
### Tue Dec 15 01:00:55 2020 +0200



### [1.5hr]Add a dishwasher. You can put in dirty dishes and it will come out as clean, neat, right?


+ It works now, tomorrow, I will add some QoL like the popup text saying that it's processing something, and if it has something inside, the popup text says like, Bowl-Clean.


+ Adding new prefabs/kitchenware to the game requires going through 2 C# files: GamePrefabData to add the prefab and GamePrefabDataBase to update the dictionary of GamePrefab and its c# class. As well as the Json config file for its cost and rarity. It's a bit all over the place, but at least I have a lot of logs and warnings, so the most time consuming part is just to wait for Unity to compile, which is painfully longer compare to the previous version of Unity. Like 15s now, compare to like 5s on Unity 2019.


+ Tomorrow, I want to change the way the game config value works, like lots of values, like dish washing time, restaurant openning time are in a static c# file, which is OKEI to use, but changing it is a full project recompile, which takes like 15s when I just want to change one variable. I will move all of them to a .txt or something config file, and a c# file to read from it in form of Key/Value. It's also make it easier to have another Cheat COnfig file, so I can quickly cheat (10s openning time, lots of money/score) with a press of a button instead of having to go to the config c# class and comment/uncomment code.


+ I also want to change the recipe name from PhoGa/PhoBo to full English so NonVietnamese speaking can understand like Pho Chicken/Pho Beef. But yeah, that's like tomorrow.