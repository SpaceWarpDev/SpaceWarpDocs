Creating Custom Parts
=====================
Disclaimer: This tutorial is for an aspect of modding not fully understood. Most of what we know is sourced by copying 
and pasting information from a very basic part, so going beyond that will have to be up to your own experimentation.

Initial Setup
-------------
To start with, we need to set up our unity development environment that we will be using to create our custom parts. 

Unity
~~~~~

1. Install `Unity 2020.3.33f1 <https://unity.com/releases/editor/whats-new/2020.3.33#release-notes>`_. That is the 
   version of unity that Kerbal Space Program 2 uses, so it is the version we need.
2. Create a new project, if you are using unity hub, ensure your editor version is set correctly.

Thunderkit
~~~~~~~~~~

3. Download the source code zip file from latest release of `ThunderKit <https://github.com/PassivePicasso/ThunderKit/releases/latest>`_ 
   on GitHub. This is a tool that will load the needed components into the Unity Project, as well as do several other 
   things outside the scope of this tutorial.
4. Extract the folder inside the downloaded zip somewhere you will remember it. Then, in Unity, open the package manager 
   by navigating to Window -> Package Manager.
5. In the package manager, click the plus icon in the top left, then add packages from disk.
6. Navigate to the downloaded folder, then open the :code:`package.json`.
7. If everything worked correctly, the ThunderKit setting window should have opened. In this window, select ThunderKit 
   Setting, then under Locate and Load game files for project select browse.
8. Navigate to your Kerbal Space Program 2 install folder (Right click on KSP 2 in steam, manage, browse local files to 
   find it if you do not know where it is) and select :code:`KSP2_x64.exe`.
9. Select Import to load the game into your project. If it shows 'API Update Required' click 'I Made a Backup. Go Ahead!'
10. When prompted, restart the project.

Addressables
~~~~~~~~~~~~

12. Re-Open the package manager, change the option at the top from Packages: In Project to Unity Registry.
13. Select Addressables, then Install. You may get some errors in your console at this step, they can (probably) be 
    safely ignored. KSP 2 has the package as well, and ThunderKit imported it, but not in a way that allowed the editor
    to access it. They likely won't actually conflict.

Finally, you will need some method of ripping unity assets. The method of which is not important to this tutorial.

Creating the part
-----------------
The first thing we need to do is create a `JSON <https://www.w3schools.com/whatis/whatis_json.asp>`_ file that describes 
the part. Opening the asset bundle that starts with :code:`parts_json-base_all` will give you an idea of the basic format. 
More research should be done to find out the extent of these settings, for now find a part closest to what you wish to 
add, and just copy and paste it into your unity project as a text asset. The one thing you need to modify, is the :code:`partName` 
entry at the top of the :code:`data` section. This is the unique ID of your part, if two parts have the same ID, that is bad, 
don't do it, so make sure you modify that field, and keep track of it.

Next create a prefab of your part. See the :code:`parts-base_assets` for the part you duplicated for examples. How to make the 
basic prefab for a part is outside the scope of this tutorial. The prefab does however need a few behaviors. On the root 
of the prefab, select Add Component, and you will need a Core Parts Data, a Module_Color, and a Module_Drag. More complex 
parts will likely need more, see the existing assets for reference. Populate these with the data from your template part. 
A lot if this data was already in your JSON, testing is needed to confirm which takes precedence.

Finally, you will need to create a sprite for your part. The default sprites are 512x512.

Making it addressable
---------------------
Now we need to actually export this in a manner that will allow the game to load it properly. In the inspector for each 
of your assets, there will be a check box for 'Addressable', Set it to true, this will tell Unity to include in when we 
build our addressable. The text field is the name by which the asset can be referenced at runtime, the two that matter 
are: the sprite must be `<partName>.png`, and the prefab must be `<partName>.prefab`, eliminating any folder structure 
that was added automatically (including `Assets`).

Once that is compelete, open the Addressables Groups with Window -> Asset Management -> Addressables -> Groups. Here is 
where you configure the export groups for your mod. Everything should be in the default local group. To get the game to 
load the json file, it needs to be labeled `parts_data`. In the labels dropown, manage labels will allow you to create 
the label.

Next, select the group, which should reveal the settings for it in the inspector. Set the Build Path to :code:`<custom>`, 
with the value :code:`Library/com.unity.addressables/aa/Windows/StandaloneWindows64`. Yes, that is the same value as it 
was by default, but Unity gets angry if you change the loading location without changing the build path. Next, set the 
load path to :code:`<custom>`, with the value :code:`{SpaceWarp.API.SpaceWarpManager.MODS_FULL_PATH}/<mod-id>/addressables/StandaloneWindows64` 
where :code:`mod-id` is the name of the folder your mod is in. This will ensure your bundles can be accessed at runtime. 

Finally, in the groups window, select Build -> New Build -> Default Build Script. This will generate the asset bundles. 
Navigate to your unity project in your file explorer, then go to :code:`Library/com.unity.addressables/aa/Windows` in 
there should be4 items including  :code:`catalog.json` and :code:`StandaloneWindows64`. Copy everything in this folder 
to a sub-folder of your mods folder, called :code:`addressables`. This will be loaded automatically by SpaceWarp.

Translations
------------
KSP 2 loads all of the text associated with the parts through the localization library, so your part  name, description, 
etc. will show up as [TBD] without localization files. In your mod directory, create a :code:`localizations` folder. In 
here, any files ending in :code:`.csv` or :code:`.i2csv` will be loaded. :code:`.i2csv` is a custom format by the 
localization library, and is beyond the scope of this tutorial.

Create a :code:`.csv` file, the name doesn't matter, as long as it ends with :code:`.csv`. Open it in a text editor that 
allows you to control the line endings (I like notepad++ for basic things like this), and ensure they are Unix style 
(:code:`lf`) not Windows style (:code:`cr-lf`). The header of the csv starts with :code:`Key,Type,Description`. These 
must be present in every file, followed by a list of languages your mod supports.

Each translation goes on its own line, with the key being what the game is looking for, type being :code:`Text` usually, 
and the description can be blank, but remember to include it. The four keys you need to have for your part are 
:code:`Parts/Title/<partName>`, :code:`Parts/Subtitle/<partName>`, :code:`Parts/Manufacturer/<partName>`, and 
:code:`Parts/Description/<partName>`. See below for an example

.. code::

   Key,Type,Description,English
   Parts/Title/truss_2v_square_1x1_custom,Text,,Custom Truss
   Parts/Subtitle/truss_2v_square_1x1_custom,Text,,TR-CU
   Parts/Manufacturer/truss_2v_square_1x1_custom,Text,,Somewhere
   Parts/Description/truss_2v_square_1x1_custom,Text,,"Definitely different from the other truss, and better too. Truss me."

Final Steps
-----------
That should be all you need, place your mod folder into the SpaceWarp Mods folder, and start KSP2. You should see your 
part in the VAB.
