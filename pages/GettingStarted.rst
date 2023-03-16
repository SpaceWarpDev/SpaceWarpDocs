Getting Started
===============

Prerequisites
-------------

1. Own a copy of KSP2
2. Have the ability to compile C# code

Project Setup
-------------

1. If you are using Visual Studio create a template with the `Space Warp Mod Template <https://github.com/jan-bures/SpaceWarp.Template>`_
2. If you are using rider, use the `Kerbal Dev <https://github.com/arthomnix/KerbalDev/>`_ plugin.
3. Copy the :code:`<KSP2 Root>/KSP2_x64_Data/Managed/Assembly-CSharp.dll` file from your game into the :code:`<project root>/external_dlls/` folder

From there you should be set with an example project, and can go from there on the wiki!

For reference your mod class extends :ref:`BaseSpaceWarpPlugin <SpaceWarp.API.Mods.BaseSpaceWarpPlugin>`

Configuration
-------------

Addendum about configuration: Space Warp now uses BepInEx's configuration api, for an example, see `Space Warp Itself <https://github.com/SpaceWarpDev/SpaceWarp/blob/main/SpaceWarp/SpaceWarpPlugin.cs>`_