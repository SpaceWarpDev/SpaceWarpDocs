.. highlight:: json
swinfo.json
===========

swinfo.json files are space warp metadata files used for checking version support and displaying information about the mod to users
any mod, even pure BepInEx mods can have an swinfo.json file that's information will be shown to the user and used for version checking by space warp


example swinfo.json 
-------------------
copied from the example mod project in the space warp repo
::
    {
        "spec": "2.0"
        "mod_id": "ExampleMod",
        "name": "Example Mod",
        "author": "Space-Warp Team",
        "description": "A Example Mod for Space-Warp",
        "source": "https://github.com/SpaceWarpDev/SpaceWarp/tree/main/ExampleMod",
        "version_check": "https://raw.githubusercontent.com/SpaceWarpDev/SpaceWarp/main/ExampleMod/swinfo.json",
        "version": "0.4.0",
        "dependencies": [],
        "conflicts" [],
        "ksp2_version": {
            "min": "0",
            "max": "1"
        }
    }

spec
----
This is the spec version for spacewarp that this mod follows, always use "2.0" here

mod_id
------
This is the ID spacewarp uses to refer to your mod, internally it is case insensitive for most things. This should be unique
::
    "mod_id": "ExampleMod"

name
----
This is the user facing name of your mod shown in the mod menu and the logs
::
    "name": "Example Mod"

author
------
Who wrote this mod
::
    "author": "Space-Warp Team"

description
-----------
A description of what the mod does
::
    "description": "A Example Mod for Space-Warp"

source
------
A link to the repository where the mods source code is contained, can be left as an empty string `""`
::
    "source": "https://github.com/SpaceWarpDev/SpaceWarp/tree/main/ExampleMod"

version_check
-------------
A link to a file hosted on the internet where space warp can check the mods version against, should link directly to another swinfo file
Optional
::
    "version_check": "https://raw.githubusercontent.com/SpaceWarpDev/SpaceWarp/main/ExampleMod/swinfo.json"

version
-------
A version string that denotes the mods version
::
    "version": "0.4.0"

dependencies
------------
A list of mod dependencies to be shown to the user and checked against
::
    "dependencies": []

Each dependency is of the following format
::
    {
        "id": "SpaceWarp",
        "version": {
            "min": "0.4.0",
            "max": "1.0.0"
        }
    }
Where id is the mod_id of the other mod, and version contains a min and max field for the range of possible versions. min or max can also be `*` for any version, or `x.*` for any patch of a certain version and so on

conflicts
---------
A list of mod dependencies to be shown to the user and checked against
::
    "conflicts": []

Each conflict is of the following format
::
    {
        "id": "SpaceWarp",
        "version": {
            "min": "0.4.0",
            "max": "1.0.0"
        }
    }
Where id is the mod_id of the other mod, and version contains a min and max field for the range of possible versions. min or max can also be `*` for any version, or `x.*` for any patch of a certain version and so on

ksp2_version
------------
The range of versions of KSP2 that this mod supports, follows the same format as a dependency.
::
    "ksp2_version": {
        "min": "0",
        "max": "1"
    }
