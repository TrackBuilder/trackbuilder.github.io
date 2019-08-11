---
layout: post
title:  "All progress update for the game. From the very beginning until 2019-08-11"
---

Sun Aug 11 01:03:55 2019 +0300 : [3hr]Huge art refactor. Add new sprite/animation for the player so that it looks like a guy, not some naked dude walking around. The animation/animator mapping took a lot of time. Add proper art for the rest of thing include: Table (4 types), redraw chopping board, trashbin, ingredient container. Also remove the change grid color code calling whenever we press A or place/remove an item. The pick/drop stuff still doesn't look right though, so will need to work more on that. But tomorrow, I will most probably try to get some gameplay vid/gif and update the website and maybe try to finish the steam page.

Sat Aug 10 16:21:38 2019 +0300 : [2hr]Finish with the food cooking/stove thing. It finally works the way I want it to. Still missing some feature like overcooking (to make food burnt or something) but I'm happy with that. Find out a pretty huge oversight that make object not registered for calling the update function. Next, I will change the human model to a slightly better looking model and some art clean up so I can create some screenshots/gifs for the website as well as the steam page.

Sat Aug 10 12:01:45 2019 +0300 : [2hr]The code finally compiles and "sort-of" works.I have the cooking code and handling and everything there and ready, with proper test for that, and code in the Stove as well as food container done. However, seems like the time calculation is not correct yet. For example, I want, like when adding Noodle (PhoBo) to the cooking pot, the total cooking time should only be 2 sec, and when adding the beef, that times goes up to 7. Right now, seems like, I add Noodle, time is 7, and when add beef, nothing change, which is not correct. Also, there is a bug with visualizing, like, I want when the food is completed, it should have some animation, but that animation check is only called when putting the ingredient in the object, which is not correct, because now, not only we have to add ingredient, we have to cook it as well.

Sat Aug 10 00:55:12 2019 +0300 : [1hr 30min]Find an even better way to deal with cooking time. Implementing, will try to finish tomorrow with proper test. I realized that all the feel like need_cooking or cooking time is not neccessary. We can find that information based on each ingredient, ie: Noodle will always take 2 second to boiled, and beef took 5 secs to boil, so we can just know that a combination of noodle and beef WILL take 7 seconds. This data can be pulled automatically from the IngredientDataJson file, thus, all our recipe data stays the same, just update to the code (addition only, no removal) and the recipe tracking in food to make that feasible. My gf is working tomorrow (Saturday) and I'm staying at home with the dog, so hopefully, I can make a lot of code.                                                        

Fri Aug 9 00:37:15 2019 +0300 : [1.5hr today, 4hr on Tue and Wed]. Trying to think the best place to put the cooking time variable, and finish the website + Steam page register. It's tricky, first, I think to just place inside the recipe data, but I now thinkg that the cooking time value should be placed even inside each ingredient itself (in the Ingredient Data Json), so that if it's existed in a recipe that needs cooking, we can even specify how long for each ingredient to cook to make things a bit easier to balance. For example: cooking a Chicken-Noodle might take 5 seconds, but a Beef-Noodle might take 8 seconds. So, to make that change, we need to make sure that, Noodle take 3 secs to cook, Chicken take 2 and Beef take 5. Also, spend Tuesday and Wednesday on registering Steam dev, and making the website. I couldn't do much this week because I had field trips from my work so it's takes more than working than usual.                            

Mon Aug 5 23:05:24 2019 +0300 : 1hr - Refactor the Rendering Offset position from the stove to table component. From now on and fix some bugs that I found with it (placing an table object to the ground somehow also its table placing function, which makes dropping a table-object to the ground being offseted, which is quite funny). All table-based object are now have a RenderingOffset transform. Didn't do much today because I have technical field trip, testing the robot at the super-market so I arrived home at like 8pm and has to go to bed early as well because I have to be early at the super market tomorrow.

Mon Aug 5 01:01:59 2019 +0300 : Add stove. Sort off. There are art and some code for it but not yet complete. We now have a stove object, that only Cookable Food Container object (like cooking pot) can be placed on, and bowl or food ingredient can not be placed on. The way it work now is just extra "if" case in the TryDropObject of the Picker function, which I don't know is ideal or not. I guess ideal case would be to have the object be able to override Can Place Object of the GridManager for its container grid, but it's wayy to much refactor for what I see as not trivial, as this might be just a one off task only. Also, working on some feature like renderer position offset so now when we placing thing on something, it can be anywhere, not just only the center, this help with the aesthetics a lot. Also, re-arrange some sprites and prefabs, so it's more tidy. I don't know, I just like moving things around.

Sat Aug 3 17:33:38 2019 +0300 : Finish with the Ingredient refactor so that it has proper transition state and stuffs like that. Looks quite nice, but I can't help but feel like something is a bit off. Next will work on oven and some general improvement.

Sat Aug 3 01:56:03 2019 +0300 : Refactor IngredientDataJson so that now it has transition data with from/to/acceptedContainer/transitionTime so we have more flexible with the code and ready the ingredient to be processed/cooked/anything. Will update the PickableIngredientComponent and the ChoppingBoard next so it's fully functioning. Move GridListenerComponent inside TableComponent. Make more sense. Some general refactor, like adding a delayed update function to the BaseComponent so no copy/paste code. Remove some code that I feel redundant and move code around a bit.

Fri Aug 2 00:50:54 2019 +0300 : Add a delegate/listener component so that whenever an item is placed, the component would know, will be useful for the chopping board and stove later in the future. First, started with the GridMapListenerComponent but I think it would be more fitting if I just make the table component automatically listen to its containing grids. Would be more useful. Didn't do a lot of things, I read manga today, and finally catch up with the latest chapter of Kaguya-Sama: Kaguya wants to be confessed to. It's actually a really decent manga. Really good, highly recommened!

Wed Jul 31 00:29:39 2019 +0300 : Kind of finish with the chopping board and the interactable component Which is component you can press [X] and do something with it. It will lock the user to it so the user can't do anything without finishing the process, or press B to cancel it and press X to speed up the process. It also has a progress bar to display the progress (while it's quite ugly). It works but need more polish and some feedback to user. Also, it kind of just hard code processing time, so we will need to add the processing time to the ingredient and a way to automatically add the processing value to the chopping board ui. Next, will try to make the oven/stove thing to heat up the pot. To make it, we will need to update the food logic, which will take time, and a sort of, world position listener component, which will need to be notified whenever an object is added to its surrounding grids. This benefit the cooking stove, but also benefit the choping board and many other thing as well.

Tue Jul 30 00:21:12 2019 +0300 : Change all the physics from 3d to 2d. It would be a lot easier to work with and more perfomance and it's more "right". Add mechanism for endless animation loop to show feedback on item that is already completed. Do a small refactor where I remove a lot of un-used stuffs and move files a round a little bit so it's more logical. I didn't finish much today because I watch Avengers Endgame with the girlfriend (it's the HD online released, we already watched in the cinema but want to see it again).

Mon Jul 29 00:30:26 2019 +0300 : Finish adding the Chopping board. The code works as you can put raw ingredient on it and it will check and process the ingredient but it's pretty barebone and code is quite hacky, so a proper refactor is needed, as well as adding a timer.

Sun Jul 28 18:35:24 2019 +0300 : Update a lot of the art, so it look passable, or, some dare I say, decent now. Will now make the chopping board so that I can process raw beef/chicken/stuffs into sliced stuffs, and probably an oven/stove next to cook thing.

Sun Jul 28 01:13:02 2019 +0300 : Spend the whole evening just to make a decent looking PhoBo Bowl. It actually looks decent now, so I'm happy, but I spend like wayyyy to much time on that, like from 10pm to 1am, with help of the girlfriend. Art is hard, but now I know a bit of what to do, so, hopefully, the next PhoGa, PhoChay and the Pot for that will be easier? Maybe.

Sat Jul 27 13:01:43 2019 +0300 : Add Food Container Data Json file to store information about Bowl and Pot, and more later on. Start to update the art a bit so it look more passable.

Fri Jul 26 00:39:17 2019 +0300 : Finally, I guess all the food and recipe stuffs are completed, I can add stuff to a pot, check if the pot is completed, and then if the pot is completed, add the whole pot as one Mixed Ingredient to the bowl. Also, add ability to empty the food-container, to put it in trash and stuffs. Next will either work on cooking/chopping, to transform food from un-cooked to cook, slightly improved art, or a serving table to serve stuffs to the customer.

Tue Jul 16 00:23:47 2019 +0300 : Add the, add food object as a ingredient to another food object. Tons of bugs around but I managed to fix it. Luckily I wrote these tests so I can test stuffs easily. Took like 2 hours just to fix bugs so I can not test (on Unity) how to add food object to another food object. Will probably lay down for 2 days or 3 to so an interview test.

Sun Jul 14 23:30:30 2019 +0300 : Fix the bug with adding the ingredient to food container (like, adding beef to a bowl). Works now. Add some quality of life change, like recipe changing color and naming in the editor for easier debugging. Next, will work with adding a food container to another food container. And then, move on to the next thing, like serving table, food request and stuff like that.

Sun Jul 14 14:56:40 2019 +0300 : Finish adding the new ingredient data and its calculation. Have a briliant idea of adding a RecipeTracking using dictionary of string and bool to make tracking of recipe much more cleaner. Also, rework with the ingredient sprite path a bit. Move the code to FoodContainer and it somehow does not work. Will check later this evening.

Sun Jul 14 00:27:51 2019 +0300 : Add the FoodContainer (Bowl, Pot, Dish ...) and their spawner as a prefab and some data object for later processing. Are able to spawn bowl and pot and stuffs. And then found a huge oversight with FoodObject and how Ingredient are added, so I'm adding more stuffs to all the food object and recipe calculation and stuffs. Hopefully, we could get something working tomorrow. Also, some refactoring and renaming stuffs to hopefully make thing slightly easier to understand.

Wed Jul 10 00:18:29 2019 +0300 : Rework the Pickable Enum, so it's type only, not a list of every possible object (Ingredient/FoodObject/FoodContainer....). More work with the food manager stuffs and add a validator to check if all of our json/food data are working in harmony with each other.

Sat Jul 6 18:14:49 2019 +0300 : Ingredient object and ingredient spawners now work with the new json/read/load data. We don't have to deal with creating new prefabs/stuff anymore. Just update the json file and add the correct path to the sprite. It will work. Next Commit will try to remove all of the old code. Commit so that if things break, there are backups to go back to.

Sat Jul 6 01:06:05 2019 +0300 : Even more refactoring, create new data class and json data file for Ingredient Object. This will contains all the data about each ingredients in game, their sprite path and possible cooking state and all. I am planning to refactor the Pickable idea a bit. So that we will not have a separate Prefab for each kind of ingredient or stuff, but just one IngredientPickable component prefab, and it can dynamically load data from the json file. Should be "better" I guess.

Fri Jul 5 00:39:04 2019 +0300 : Add cooking phase checking for the Food_Object so that object have to be put in proper phase. Refactor the FoodManager a bit so it's nicer. Start working on the actual displaying and interacting part in Unity now. Hopefully, I can get the Mock_Pho_Ga things up and running, and probably I would want a test to check for resources in all file in recipe as well.

Thu Jul 4 00:42:01 2019 +0300 : Update json data to contains all the recipe sprite. Update the FoodObject to have a reference to its container, as the FoodObject will be spawn whenever a FoodContainer is pulled out. Also add the function to find recipe with a certain container type. Will need some validation code to check that all sprite in the json are loadable.  And maybe remove all the container/pickable enum.

Tue Jul 2 00:02:28 2019 +0300 : Add some place holder assets to get up with the programming part. I tried to draw something but it looks like crap, so it's not working.

Mon Jul 1 00:11:39 2019 +0300 : Fix food object so that it works better. I will integrate it to the unity code now. It's been just data flowing around for too long. No visible progress at all. Art is problemmatic, because I can't draw anything, but I will try to just draw square and circle with text inside, for now. Until I can find an artist.

Sun Jun 30 01:48:35 2019 +0300 : Finish the first iteration of code/logic/data for the FoodObject/Recipe stuffs as well as their unittest. Works for single ingredient but does not work for combination recipe. Something is wrong. Must check!Fri Jun 28 00:36:29 2019 +0300 : Finish the part that check for adding a new ingredient to a recipe and automatically form a new recipe. Have some trouble with Adding TWO ingredients of the same type to a recipe, might cause trouble. Have a code to fix it but I'm not entirely sure about that, so maybe we can inform a RULE that one recipe can not have 2 SAME ingredients. Also, see some warning from Unity about too deep serialization due to the way GameRecipe can contains list of GameRecipe, which is quite recursively, but it should not be a problem.

Thu Jun 27 01:17:37 2019 +0300 : Add the Game Recipe class, each contain a list of other Game Recipe (I called them Combination Recipe, while the food to serve to customer call Food Recipe), and list of ingredients. It took a while to think of the good data structure (it still isn't perfect anyway) and next, will work on how to dynamically create a food object, like, if you add a Vegetable to a dish, it knows that it's not a valid, you have to add, for example, BanhPho, and it will know that you are trying to make PhoBo or PhoGa, and if you after that, add like rice to that, it will not accept it.

Wed Jun 26 00:08:49 2019 +0300 : Add better visualization for the ingredient and recipe, so in the data, we would see proper object name, instead of enum number. Also, discuss with the master chief of the house and decide that the making of Pho has to be even more complicated, so our data structure has to be even more refined.

Tue Jun 25 00:11:58 2019 +0300 : Make a function to print object data to json format so we could save it by copy/paste, and make it as foundation for later on change in the object structure. Will work on recipe and food tomorrow.

Sat Jun 22 00:44:12 2019 +0300 : Add Json save/load for recipe data object. It's a bit funny as somehow it's 2019 and Unity does not support saving an array/list object to json but we have to use a wrapper for that. Silly.

Tue Jun 18 23:58:31 2019 +0300 : Add chicken and beef prefabs as well as their containers. Move some files around, I might wanna do the refactor and read data from json first before doing the recipe, because that seems to be better than jump straight into it.

Mon May 27 01:09:40 2019 +0300 : Some arts and recipe data class. Add some new arts from humble bundle and remove old and unmatch art. Add a recipe data class as a backbone for recipe generation and stuffs.

Sat May 25 01:18:33 2019 +0300 : Start working on this again after a long delay because I was doing my thesis. Slow catch up and write all the container and stuffs. Everything seems to work fine now.

Sun Mar 17 14:18:19 2019 +0200 : Continue to work with the container to drop/get object. Moving files around as well. Right now, using a data-type object to pass around. If I put an object into a container, it despawn the object, and push the object's data into the container only, seems way better. But it's quite messy so I will try to think of some better way for the data to work.

Fri Mar 15 01:20:31 2019 +0200 : Finish with the container component and trash can. There is a bug that if you place a pickable object inside a container that is also pickable (for example: food into bowl), it can't be picked anymore, which is weird

Thu Mar 14 00:38:59 2019 +0200 : Add 2 new pixel arts for Pho and a bowl of Pho. Will work on the container stuffs now, include a bowl, trash can and stuffs.

Mon Mar 11 00:34:35 2019 +0200 : Add heavy pickable component, so object like table, or food chest, heavy one, would also be pickable by pressing L + R. It's important to separate between heavy and light weight object, so player won't mistakenly grab table when they just want to get a tomato or something. Remove a lot of previous code. This time, our code looks much more neat. Let's hope it will still be neat and clean after we add tons more feature.

Mon Mar 4 00:18:13 2019 +0200 : Finish with the Grid rework. Seems to work really well now, we now have table/pickable component and a box to get stuffs from it. Will try to make a Heavy pickable next? and push/pull and clean up.

Sat Mar 2 01:10:02 2019 +0200 : More update on grid map and grid manager. We could place on the gridmap now, just need to communicate it to the grid cell. It's already seems to be better now. Much more clean now.

Fri Mar 1 00:11:10 2019 +0200 : Rework the grid thing and possibly the whole pickup/drop down system. Well, it's good to know what doesn't work. Right. Don't have much time to code much this evening so I just create the GridCell and some foundation. Hope to get it work tomorrow.

Tue Feb 26 00:17:25 2019 +0200 : Heavy Pickable Component, for stuff like Table/Chest and later, more stuffs. It's the stuff that is really heavy that maybe should only be picked during planning phase. Another idea would be to have a "lock" function, for example, chest, we could lock it and then move it around. But then it kind of creates problem for other stuffs as well. I dunno.

Sun Feb 24 23:50:35 2019 +0200 : Grid maps overlay, fairly bad performance though, will need a more proper solution to go on. Pickable item can't be place on ground now. Tweaking movement collider and picking transform so it feels slightly better/easier to pickup/drop stuffs. Next, maybe try to do a HEAVY PICKABLE component, so like, we hold (A) or (L) and (R) at same time to be able to pick TABLE or Heavy object.

Sun Feb 24 00:38:59 2019 +0200 : Table works. Rework camera to be just normal cam. Will try to make food/stuffs smaller and kick-able around. Fix all the collider a bit so player movement will be easier. Make Long hold to pickup Big stuffs, like table and chest?

Sat Feb 23 14:44:04 2019 +0200 : Fixing the Grid, works perfectly now. Add the container back so that it also works with the grid. Add a small square indicator so we know where the player is placing the cursor

Sat Feb 23 01:38:01 2019 +0200 : Add GRID map, now we don't use shpere cast and stuff anymore, we use a grid map to get stuffs. No use of Unity Physis anymore, which I guess should be better in the long term since we have more control of it. And we don't need fancy Physic stuff anyway, we just use it for like, finding object in areas, which it doesn't do a good job.

Fri Feb 22 00:16:06 2019 +0200 : Add container component that can store pickable object. Refactor the physis a bit so we use rigidbody and collider 3d now, instead of 2d cuz I wanna go 3d now. There is a bug with try grabbing object using SphereCastAll, it sometimes go wayy to far, need some researching

Thu Feb 21 00:01:55 2019 +0200 : Add DOTween libs and PickerComponent from ControllableObject. DOTween to make some nice dope animation. PickerComponent so that it's now separated from the PlayerObject, make code less spaghetti in the long turn I hope. Try to add the container component, to contain object, but that need the Picker Component, which I did, and it's late in the evening now, so I will work on that tomorrow.

Wed Feb 20 00:50:04 2019 +0200 : Slight refactor for the interactable component and pickable compoent so it's even more clear. Make a round up function, so object being putted down will always stay in rounded up position, will make it great for the grid layout. Make a mistake of having the box being the child of the picker transform fron the controllable object instead of the holder object, but this seems nice, so I will let it be. Will import Tween next, so when we pickup/drop object, there will be some feedback to the player because it doesn't feel clear now.

Tue Feb 19 00:37:37 2019 +0200 : Refactor player controller, it's now a separated component to added to controllable object, which should make it easier to go with AI and stuffs. Player can now pick up and drop object. It's a component now, but I want to divide it even more. The picked up object should have a check to see if it can be interacted with as well (to prevent multi-player picking up the same object).

Sat Feb 16 20:42:56 2019 +0200 : Add 8 directional animation for run and idle and proper controller. Also try to add a pick up component, using Physic Circle Cast. Works but buggy. Will try to use Unity Grid next.

Fri Feb 15 23:52:13 2019 +0200 : Finish with the camera controller and split camera. Also create the players manager to separate it from the input manager. It's still a bit tangled within each other but I think that's ok for now. Will work on animation tomorrow.

Fri Feb 15 00:14:22 2019 +0200 : Update the Input Controller and the rest so that it can automatically spawn number of player based on a number. Camera also follow suit. Next, will try to make the camera follow the player and split screen.

Thu Feb 14 00:06:35 2019 +0200 : Update README.md

Thu Feb 14 00:06:23 2019 +0200 : Update README.md

Thu Feb 14 00:03:05 2019 +0200 : First commit. Small working movement engine going and rewire for controller movement working. It's really good.

Wed Feb 13 23:56:45 2019 +0200 : Initial commit