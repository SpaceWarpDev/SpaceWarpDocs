modinfo.json
=========================================

The modinfo.json file for a mod follows the following structure

::

   {
       "mod_id": "example_mod", // Should be the same as the folder name for the mod
       "author": "cheese3660",
       "name": "Example Mod",
       "description": "An example mod for spacewarp",
       "source": "https://github.com/X606/SpaceWarp", // Link to the source repository, none for no source
       "version": "0.0.1",
       "dependencies": [
           {
               "id": "example_dependency",
               "version": {
                   "min": "0.0.1",
                   "max": "*" //any field in the semantic version can be replaced with star, or if there is no ., the '*' is implied
               }
           },
           .
           .
           .
       ],
       "ksp2_version": {
           "min": "0.0.0",
           "max": "*"
       }
   }
