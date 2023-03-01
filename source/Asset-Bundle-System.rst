Asset Bundle Loading System
===========================

As of 0.2.0 Space Warp provides an asset bundle loader that loads and caches all assets under `SpaceWarp/assets/bundles` for internal Space Warp assets and `ModFolder/assets/bundles`

Asset bundles must have a .bundle extension

Imports
-------

::

    using SpaceWarp.API.AssetBundles

Methods
-------

**public static T ResourceManager.GetAsset<T>(string path) where T : UnityEngine.Object**

This loads an asset from a path and throws if it can't

**public static bool ResourceManager.TryGet<T>(string path, out T asset) where T : UnityEngine.Object**

This loads an asset from a path, and returns true if successful, otherwise, it returns false and sets asset to null

Paths
-----

Paths are of the following format:

- `[mod_id]/[bundle name without .bundle]/[path to asset in bundle without assets/]`
- For Space Warp internal assets: `space_warp/[bundle name without .bundle]/[path to asset in bundle without assets/]/`
