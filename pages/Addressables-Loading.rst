Addressables Loading
====================

This tutorial provides information on addressables loading

Creating Addressables
---------------------

Setup
^^^^^

This subsection provides information on what is necessary to be done to create addressable bundles

Unity
~~~~~

1. Install `Unity 2020.3.33f1 <https://unity.com/releases/editor/whats-new/2020.3.33#release-notes>`_. That is the 
   version of unity that Kerbal Space Program 2 uses, so it is the version we need.
2. Create a new project, if you are using unity hub, ensure your editor version is set correctly.

ThunderKit
~~~~~~~~~~

1. Download the source code zip file from latest release of `ThunderKit <https://github.com/PassivePicasso/ThunderKit/releases/latest>`_ 
   on GitHub. This is a tool that will load the needed components into the Unity Project, as well as do several other 
   things outside the scope of this tutorial.
2. Extract the folder inside the downloaded zip somewhere you will remember it. Then, in Unity, open the package manager 
   by navigating to Window -> Package Manager.
3. In the package manager, click the plus icon in the top left, then add packages from disk.
4. Navigate to the downloaded folder, then open the :code:`package.json`.
5. If everything worked correctly, the ThunderKit setting window should have opened. In this window, select ThunderKit 
   Setting, then under Locate and Load game files for project select browse.
6. Navigate to your Kerbal Space Program 2 install folder (Right click on KSP 2 in steam, manage, browse local files to 
   find it if you do not know where it is) and select :code:`KSP2_x64.exe`.
7. Select Import to load the game into your project. If it shows 'API Update Required' click 'I Made a Backup. Go Ahead!'
8.  When prompted, restart the project.

Addressables
~~~~~~~~~~~~

12. Re-Open the package manager, change the option at the top from Packages: In Project to Unity Registry.
13. Select Addressables, then Install. You may get some errors in your console at this step, they can (probably) be 
    safely ignored. KSP 2 has the package as well, and ThunderKit imported it, but not in a way that allowed the editor
    to access it. They likely won't actually conflict.

Mod Side
~~~~~~~~

14. In your mods Space Warp Plugin class, add the following static field :code:`public static string Path { get; private set; }`
15. And then in the :code:`OnPreInitialize()` method of your mod add :code:`Path = PluginFolderPath`

Creation
^^^^^^^^

Marking assets as Addressable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For each asset that you wish to make addressable, in the inspector, there should be a check box for 'Addressable', which needs to be set to true. The text field is then the name which the asset is referenced by at runtime.

Configure Addressable Groups
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Open the addressables groups via :code:`Window -> Asset Management -> Addressables -> Groups`
2. Make sure everything is in the default local group
3. Add all labels you need to to the group with the labels drop down (example: for parts the group must have the :code:`parts_data` label)
4. Select the group to reveal its settings
5. Set the buildpath to :code:`<custom>` with the value :code:`Library/com.unity.addressables/aa/Windows/StandaloneWindows64`
6. Set the loadpath to :code:`<custom>` with the value :code:`{MOD_CLASS.Path}/addressables/StandaloneWindows64` where mod_class is the full name of your mods class with namespaces

Building Addressables
~~~~~~~~~~~~~~~~~~~~~
1. In the groups window select :code:`Build -> New Build -> Default Build Script`
2. Navigate to your project in the file explorer and go to :code:`Library/com.unity.addressables/aa/Windows`
3. Check there is a :code:`catalog.json` and :code:`StandaloneWindows64` in this directory
4. If there is, copy everything in the folder to the :code:`addressables` subfolder of your mod, if there isn't then something went wrong.

