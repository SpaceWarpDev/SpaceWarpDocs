Asset Loading
=============

:ref:`AssetManager <SpaceWarp.API.Assets.AssetManager>` overview
---------------------

Space Warp has an :code:`AssetManager` class that is under the :code:`SpaceWarp.API.Assets` namespace.

Its primary purpose is to statically cache all non-addressable assets used by space warp dependent mods under the following path schema, :code:`mod_id/<type_identifier>/path_to_asset`, case insensitive.

To then read these assets it provides the following user facing methods.

:code:`public static T GetAsset<T>(string path) where T : UnityEngine.Object`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This method gets an asset located at the path :code:`path`, and throws an exception if it cannot.

:code:`public static bool TryGetAsset<T>(string path, out T asset) where T : UnityObject`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This does the same as above, but instead of throwing, it returns false and sets asset to null if it cannot load the path, otherwise it returns true and sets the asset to the asset at that path.

Asset Bundle Loading
--------------------

Space Warp automatically loads all asset bundles under the :code:`<mod>/assets/bundles` folder. But the asset bundle must have a :code:`.bundle` extension to be loaded

It will load all assets into a path transformation that looks like the following, given this is the path layout of your asset bundle, and your mod id is :code:`cool_mod`
::
    coolBundle.bundle
    |
    \-- Assets
        |
        +-- coolBundle
        |   |
        |   \-- image.png -> `cool_mod/coolbundle/image.png`
        |
        +-- coolShaders
        |   |
        |   \-- god.shader -> `cool_mod/coolbundle/coolshaders/god.shader`   
        |
        +-- coolObject.prefab -> `cool_mod/coolbundle/coolobject.prefab`

As we can see from above, the paths are all lowercase, start with the mod_id followed by the bundle name without the bundle extension, then the file name without the assets folder name, or if the folder its under is the same name as the bundle, w/o that.


Image Texture loading
---------------------

Space Warp will also automatically load all images under the :code:`<mod>/assets/images` folder. It will go through the entire directory tree to load these. It loads them as assets of type :code:`Texture2D` and puts them in the following path, :code:`<mod_id>/images/<path_to_image_relative_to_folder>`


