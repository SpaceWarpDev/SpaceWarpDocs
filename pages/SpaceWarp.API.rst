.. highlight:: cs
*************
SpaceWarp.API
*************

This page contains documentation on every single space warp api class, function, etc...

It will contain sections for the namespaces, subsections for the classes, and subsubsections for methods


SpaceWarp.API.Assets
====================

This contains classes relating to Space Warps asset system

SpaceWarp.API.Assets.AssetManager
---------------------------------
Also described in :ref:`Asset Loading`

This is a static class containing methods for loading assets that spacewarp has loaded

public static T GetAsset<T>(string path) where T : UnityEngine.Object
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This method gets an asset located at the path :code:`path`, and throws an exception if it cannot.

public static bool TryGetAsset<T>(string path, out T asset) where T : UnityObject
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This does the same as above, but instead of throwing, it returns false and sets asset to null if it cannot load the path, otherwise it returns true and sets the asset to the asset at that path.

SpaceWarp.API.Game
==================

This contains API with direct relation to the game, except for UI which is in :ref:`SpaceWarp.API.UI`

SpaceWarp.API.Game.Vehicle
--------------------------

This is a static class that at the moment provides a few getter properties for getting active vehicles and such

public static VesselVehicle ActiveVesselVehicle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This returns the active vehicle in the currently running game as a VesselVehicle

public static VesselComponent ActiveSimVessel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This returns the active vessel's :code:`VesselComponent` component

SpaceWarp.API.Game.Extensions
=============================

This contains all the extension methods for the game.

SpaceWarp.API.Game.Extensions.PartProviderExtensions
----------------------------------------------------

This is a static class that contains extension methods for the games :code:`PartProvider` class.

The active part provider can be grabbed in your mod class as :code:`Game.Parts`

public static IEnumerable<PartCore> WithModule<T>(this PartProvider provider) where T : ModuleData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This allows you to grab all parts that the game knows about that have a certain module, can be used for replacing the module or adding onto it, or modifying it.

Example
::
    foreach (var part in Game.Parts.WithModule<Antenna>) {
        part.modules.add(new CoolerAntenna())
    }

SpaceWarp.API.Game.Extensions.VesselVehicleExtensions
-----------------------------------------------------

This is a static class that contains extension methods for the :code:`VesselVehicle` class, to add methods to do commonly done things.

public static void SetMainThrottle(this VesselVehicle vehicle, float throttle)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This function is used to set the vehicles throttle to :code:`throttle`, the throttle should be between 0.0 and 1.0

public static void SetRoll(this VesselVehicle vehicle, float roll)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This function is used to set the roll field of the vehicles flight controls.

public static void SetYaw(this VesselVehicle vehicle, float yaw)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This function is used to set the yaw field of the vehicles flight controls.

public static void SetPitch(this VesselVehicle vehicle, float pitch)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This function is used to set the pitch field of the vehicles flight controls.

public static void SetRollYawPitch(this VesselVehicle vehicle, float roll, float yaw, float pitch)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This function is used to set the roll, yaw, and pitch of the vehicles flight controls.

public static void SetRollTrim(this VesselVehicle vehicle, float rollTrim)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This function is used to set the roll trim of the vehicle.

public static void SetYawTrim(this VesselVehicle vehicle, float yawTrim)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This function is used to set the yaw trim of the vehicle.

public static void SetPitchTrim(this VesselVehicle vehicle, float pitchTrim)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This function is used to set the pitch trim of the vehicle.

public static void SetRollYawPitchTrim(this VesselVehicle vehicle, float rollTrim, float yawTrim, float pitchTrim)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This function is used to set the roll yaw and pitch trim of the vehicle.

public static void SetInputRoll(this VesselVehicle vehicle, float roll)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This function is used to set the input roll of the vehicle.

public static void SetInputYaw(this VesselVehicle vehicle, float yaw)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This function is used to set the input yaw of the vehicle.

public static void SetInputPitch(this VesselVehicle vehicle, float pitch)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This function is used to set the input pitch of the vehicle.

public static void SetInputRollYawPitch(this VesselVehicle vehicle, float roll, float yaw, float pitch)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This function is used to set the input roll yaw and pitch of the vehicle.

public static void SetWheelSteer(this VesselVehicle vehicle, float wheelSteer, float? wheelSteerTrim=null)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This function is used to set the wheel steer and trim of the vehicle.

public static void SetWheelThrottle(this VesselVehicle vehicle, float wheelThrottle, float? wheelThrottleTrim=null)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This function is used to set the wheel throttle and trim of the vehicle.

public static void SetXYZ(this VesselVehicle vehicle, float? X = null, float? Y = null, float? Z = null)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This function is used to set the vehicle's flight control X,Y, and Z fields.
If any value is null, that field does not get updated.

public static void SetXYZ(this VesselVehicle vehicle, Vector3 XYZ)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This function is used to set the vehicle's flight control X, Y, and Z fields with a unity vector.

public static void SetKillRot(this VesselVehicle vehicle, bool killRot)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This sets the kill rotation input for the vehicle.

public static void SetGearState(this VesselVehicle vehicle, bool up)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This sets the gear state input for the vehicle.

public static void SetHeadlight(this VesselVehicle vehicle, bool on)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This sets the headlight input for the vehicle.

public static void SetBrake(this VesselVehicle vehicle, bool on)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This sets the break input for the vehicle.

public static void SetStage(this VesselVehicle vehicle, bool stage)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This sets the stage input for the vehicle.

SpaceWarp.API.Game.Messages
===========================

This contains all messaging abstractions for the game.

SpaceWarp.API.Game.Messages.StateChanges
----------------------------------------

This adds events that mods can subscribe to whenever a certain state is entered or left, or the state changes.

public static event Action<GameStateEnteredMessage> InvalidStateEntered
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The argument to this is the games :code:`GameStateEnteredMessage` that it publishes

It is published when the invalid state state is entered

public static event Action<GameStateEnteredMessage> WarmUpLoadingStateEntered
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The argument to this is the games :code:`GameStateEnteredMessage` that it publishes

It is published when the warm up loading state state is entered

public static event Action<GameStateEnteredMessage> MainMenuStateEntered
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The argument to this is the games :code:`GameStateEnteredMessage` that it publishes

It is published when the main menu state state is entered

public static event Action<GameStateEnteredMessage> KerbalSpaceCenterStateEntered
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The argument to this is the games :code:`GameStateEnteredMessage` that it publishes

It is published when the kerbal space center state state is entered

public static event Action<GameStateEnteredMessage> VehicleAssemblyBuilderEntered
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The argument to this is the games :code:`GameStateEnteredMessage` that it publishes

It is published when the vehicle assembly builder state is entered

public static event Action<GameStateEnteredMessage> BaseAssemblyEditorEntered
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The argument to this is the games :code:`GameStateEnteredMessage` that it publishes

It is published when the base assembly editor state is entered

public static event Action<GameStateEnteredMessage> FlightViewEntered
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The argument to this is the games :code:`GameStateEnteredMessage` that it publishes

It is published when the flight view state is entered

public static event Action<GameStateEnteredMessage> ColonyViewEntered
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The argument to this is the games :code:`GameStateEnteredMessage` that it publishes

It is published when the colony view state is entered

public static event Action<GameStateEnteredMessage> Map3DViewEntered
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The argument to this is the games :code:`GameStateEnteredMessage` that it publishes

It is published when the map3d view state is entered

public static event Action<GameStateEnteredMessage> PhotoModeEntered
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The argument to this is the games :code:`GameStateEnteredMessage` that it publishes

It is published when the photo mode state is entered

public static event Action<GameStateEnteredMessage> MetricsModeEntered
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The argument to this is the games :code:`GameStateEnteredMessage` that it publishes

It is published when the metrics mode state is entered

public static event Action<GameStateEnteredMessage> PlanetViewerEntered
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The argument to this is the games :code:`GameStateEnteredMessage` that it publishes

It is published when the planet viewer state is entered

public static event Action<GameStateEnteredMessage> LoadingEntered
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The argument to this is the games :code:`GameStateEnteredMessage` that it publishes

It is published when the loading state is entered

public static event Action<GameStateEnteredMessage> TrainingCenterEntered
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The argument to this is the games :code:`GameStateEnteredMessage` that it publishes

It is published when the training center state is entered

public static event Action<GameStateEnteredMessage> MissionControlEntered
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The argument to this is the games :code:`GameStateEnteredMessage` that it publishes

It is published when the mission control state is entered

public static event Action<GameStateEnteredMessage> TrackingStationEntered
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The argument to this is the games :code:`GameStateEnteredMessage` that it publishes

It is published when the tracking station state is entered

public static event Action<GameStateEnteredMessage> ResearchAndDevelopmentEntered
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The argument to this is the games :code:`GameStateEnteredMessage` that it publishes

It is published when the research and development state is entered

public static event Action<GameStateEnteredMessage> LaunchpadEntered
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The argument to this is the games :code:`GameStateEnteredMessage` that it publishes

It is published when the launchpad state is entered

public static event Action<GameStateEnteredMessage> RunwayEntered
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The argument to this is the games :code:`GameStateEnteredMessage` that it publishes

It is published when the runway state is entered

public static event Action<GameStateEnteredMessage> FlagEntered
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The argument to this is the games :code:`GameStateEnteredMessage` that it publishes

It is published when the flag state is entered

public static event Action<GameStateLeftMessage> InvalidStateLeft
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The argument to this is the games :code:`GameStateLeftMessage` that it publishes

It is published when the invalid state state is left

public static event Action<GameStateLeftMessage> WarmUpLoadingStateLeft
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The argument to this is the games :code:`GameStateLeftMessage` that it publishes

It is published when the warm up loading state state is left

public static event Action<GameStateLeftMessage> MainMenuStateLeft
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The argument to this is the games :code:`GameStateLeftMessage` that it publishes

It is published when the main menu state state is left

public static event Action<GameStateLeftMessage> KerbalSpaceCenterStateLeft
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The argument to this is the games :code:`GameStateLeftMessage` that it publishes

It is published when the kerbal space center state state is left

public static event Action<GameStateLeftMessage> VehicleAssemblyBuilderLeft
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The argument to this is the games :code:`GameStateLeftMessage` that it publishes

It is published when the vehicle assembly builder state is left

public static event Action<GameStateLeftMessage> BaseAssemblyEditorLeft
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The argument to this is the games :code:`GameStateLeftMessage` that it publishes

It is published when the base assembly editor state is left

public static event Action<GameStateLeftMessage> FlightViewLeft
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The argument to this is the games :code:`GameStateLeftMessage` that it publishes

It is published when the flight view state is left

public static event Action<GameStateLeftMessage> ColonyViewLeft
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The argument to this is the games :code:`GameStateLeftMessage` that it publishes

It is published when the colony view state is left

public static event Action<GameStateLeftMessage> PhotoModeLeft
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The argument to this is the games :code:`GameStateLeftMessage` that it publishes

It is published when the photo mode state is left

public static event Action<GameStateLeftMessage> Map3DViewLeft
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The argument to this is the games :code:`GameStateLeftMessage` that it publishes

It is published when the map3d view state is left

public static event Action<GameStateLeftMessage> MetricsModeLeft
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The argument to this is the games :code:`GameStateLeftMessage` that it publishes

It is published when the metrics mode state is left

public static event Action<GameStateLeftMessage> PlanetViewerLeft
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The argument to this is the games :code:`GameStateLeftMessage` that it publishes

It is published when the planet viewer state is left

public static event Action<GameStateLeftMessage> LoadingLeft
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The argument to this is the games :code:`GameStateLeftMessage` that it publishes

It is published when the loading state is left

public static event Action<GameStateLeftMessage> TrainingCenterLeft
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The argument to this is the games :code:`GameStateLeftMessage` that it publishes

It is published when the training center state is left

public static event Action<GameStateLeftMessage> MissionControlLeft
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The argument to this is the games :code:`GameStateLeftMessage` that it publishes

It is published when the mission control state is left

public static event Action<GameStateLeftMessage> TrackingStationLeft
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The argument to this is the games :code:`GameStateLeftMessage` that it publishes

It is published when the tracking station state is left

public static event Action<GameStateLeftMessage> ResearchAndDevelopmentLeft
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The argument to this is the games :code:`GameStateLeftMessage` that it publishes

It is published when the research and development state is left

public static event Action<GameStateLeftMessage> LaunchpadLeft
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The argument to this is the games :code:`GameStateLeftMessage` that it publishes

It is published when the launchpad state is left

public static event Action<GameStateLeftMessage> RunwayLeft
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The argument to this is the games :code:`GameStateLeftMessage` that it publishes

It is published when the runway state is left

public static event Action<GameStateLeftMessage> FlagLeft
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The argument to this is the games :code:`GameStateLeftMessage` that it publishes

It is published when the flag state is left

public static event Action<GameStateChangedMessage, GameState, GameState> GameStateChanged`

The arguments to this are as follows.

1. The GameStateChangedMessage that the game publishes
2. The state that is being left
3. The state that is being entered

This is published anytime the game state changes.

SpaceWarp.API.Mods
==================

This API section contains classes related to space warp mods.

SpaceWarp.API.Mods.BaseSpaceWarpPlugin
--------------------------------------

This is the class that all space warp mods should derive, it derives BepInEx's BaseUnityPlugin class but provides space warp specific features

protected static GameInstance Game
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is a getter for the currently active game instance of KSP2.

protected MessageCenter Messages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is a getter for said instance's MessageCenter

protected ContextualFxSystem CFXSystem
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is a getter for the active CFXSystem

protected bool IsGameShuttingDown
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is a getter that is true when the game is shutting down.

public :ref:`ModInfo <SpaceWarp.API.Mods.JSON.ModInfo>` SpaceWarpMetadata
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This stores the mods metadata

It is set by space warp before :ref:`OnPreInitialized <public virtual void OnPreInitialized()>`

public string PluginFolderPath
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is a getter for the current mods plugin folder path, used for useful things like addressables.

Set at the same time as :ref:`SpaceWarpMetadata <public ModInfo SpaceWarpMetadata>`

public virtual void OnPreInitialized()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is the 1st stage initialization method your mod should override.

This is called before any of the game is actually loaded, it is called as early as possible in the games bootstrap process.

public virtual void OnInitialized()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is the 2nd stage initialization method your mod should override.

This is called after the game is loaded, and after your mods assets are loaded.

public virtual void OnPostInitialized()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is the 3rd stage initialization method your mod should override

This is called after all mods have done first stage initialization

SpaceWarp.API.Mods.GlobalModDefines
-----------------------------------

This class contains static definitions that are useful for mods, such as the location of asset folders.

public static readonly string AssetBundlesFolder
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This getter contains the offset to the asset bundles folder from the mods base path.

public static readonly string ImageAssetsFolder
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This getter contains the offset to the image assets folder from the mods base path.

SpaceWarp.API.Mods.JSON
=======================

This contains the JSON classes used by space warp for metadata.

SpaceWarp.API.Mods.JSON.DependencyInfo
--------------------------------------

This contains information about a dependency.

public string ID
^^^^^^^^^^^^^^^^^^^^^^^^

This is a getter for the mod id of the dependency

public :ref:`SupportedVersionsInfo <SpaceWarp.API.Mods.JSON.SupportedVersionsInfo>` Version
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is a getter for the version info of the dependency

SpaceWarp.API.Mods.JSON.ModInfo
-------------------------------

This class contains all the metadata for a space warp mod

public string ModID
^^^^^^^^^^^^^^^^^^^

This is a getter for the mods ModID, as used by space warp

public string Name
^^^^^^^^^^^^^^^^^^

This getter contains the mods user friendly name

public string Author
^^^^^^^^^^^^^^^^^^^^

This getter contains the author of the mod

public string Description
^^^^^^^^^^^^^^^^^^^^^^^^^

This getter contains the description of the mod.

public string Source
^^^^^^^^^^^^^^^^^^^^

This getter contains the link to the source code of the mod.

public string Version
^^^^^^^^^^^^^^^^^^^^^

This getter contains the version of the mod.

public List<:ref:`DependencyInfo <SpaceWarp.API.Mods.JSON.DependencyInfo>`> Dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This getter contains a list of the mods dependencies

public :ref:`SupportedVersionsInfo <SpaceWarp.API.Mods.JSON.SupportedVersionsInfo>` Version
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This getter contains the KSP 2 versiuons this mod accepts

public string VersionCheck
^^^^^^^^^^^^^^^^^^^^^^^^^^

This getter if not null contains a link to the online version of the mod info which version checking can be done with

SpaceWarp.API.Mods.JSON.SupportedVersionsInfo
---------------------------------------------

This class contains a range of acceptable versions for either a dependency or for KSP

public string Min
^^^^^^^^^^^^^^^^^

This contains the minimum supported version

public string Max
^^^^^^^^^^^^^^^^^

This contains the maximum supported version

public bool IsSupported(string toCheck)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns if :code:`toCheck` is within the range of supported versions.

SpaceWarp.API.UI
================

This contains API related to the games UI and space warps UI

SpaceWarp.API.UI.MainMenu
-------------------------

This static class contains API related to the main menu.

public static void RegisterMenuButton(string name, Action onClicked)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This function adds a button to the main menu, where the action gets published when the button is clicked.

SpaceWarp.API.UI.Skins
----------------------

This contains space warps UI skinning

public static GUISkin ConsoleSkin
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This getter returns the skin for the console.

SpaceWarp.API.UI.Appbar
=======================

These contain classes relating to the games appbar

SpaceWarp.API.UI.Appbar.Appbar 
------------------------------

This class contains methods related to registering buttons on the Appbar

public static T RegisterGameAppbarMenu<T>(string text, string title, string id, Sprite icon) where T : :ref:`AppbarMenu <SpaceWarp.API.UI.Appbar.AppBarMenu>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This method creates an AppBarMenu to be on the in flight Appbar, it then returns this menu.

- :code:`text`: The text on the appbar button created for this menu
- :code:`title`: The title of the menu being created
- :code:`id`: The ID for the button on the appbar
- :code:`icon`: The icon for the button on the appbar

public static T RegisterGameAppbarMenu<T>(string text, string title, string id, Texture2D icon) where T : :ref:`AppbarMenu <SpaceWarp.API.UI.Appbar.AppBarMenu>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This does the same as the one above, except it uses a Texture2D instead of a sprite

public static void RegisterAppButton(string text, string id, Sprite icon, Action<bool> func)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This method registers an appbar button on the in flight app bar

- :code:`text`: The text for the button
- :code:`id`: The ID of the button
- :code:`icon`: The icon for the button
- :code:`func`: The action that gets called when the button is toggled, it gets passed whether its being turned on or off.

public static void RegisterAppButton(string text, string id, Texture2D icon, Action<bool> func)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This does the same as the one above, except it uses a Texture2D instead of a sprite

public static void RegisterOABAppButton(string text, string id, Sprite icon, Action<bool> func)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This method registers an appbar button on the OAB app bar

- :code:`text`: The text for the button
- :code:`id`: The ID of the button
- :code:`icon`: The icon for the button
- :code:`func`: The action that gets called when the button is toggled, it gets passed whether its being turned on or off.

public static void RegisterOABAppButton(string text, string id, Texture2D icon, Action<bool> func)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This does the same as the one above, except it uses a Texture2D instead of a sprite

public static Sprite GetAppBarIconFromTexture(Texture2D texture, int width=0, int height=0)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This converts a Texture2D to a appbar icon

- :code:`texture`: the texture to be converted
- :code:`width`: the width of the resultant sprite, 0 for inference
- :code:`height`: the height of the resultant sprite, 0 for inference

public static void SetAppBarButtonIndicator(string id, bool indicator)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets an app bar buttons indicator (the green sprite to the side of it)

- :code:`id`: The id of the button, what you set when registering the app bar button
- :code:`indicator`: The state of the indicator, true for on, false for off

SpaceWarpAPI.UI.Appbar.AppbarMenu
---------------------------------

This is an abstract class that can be extended to implement an app bar menu

public abstract float Width
^^^^^^^^^^^^^^^^^^^^^^^^^^^

This abstract getter is used for menu width

public abstract float Height
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This abstract getter is used for menu height.

public abstract float X
^^^^^^^^^^^^^^^^^^^^^^^

This abstract getter is used for the X position of the menu

public abstract float Y
^^^^^^^^^^^^^^^^^^^^^^^

This abstract getter is used for the Y position of the menu

public virtual GUISkin Skin
^^^^^^^^^^^^^^^^^^^^^^^^^^^

This virtual getter is used for the skin of the menu, by default it uses space warps

public abstract void DrawWindow(int windowID)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This abstract function must be implemented to draw the window, its a simple IMGui window draw function.