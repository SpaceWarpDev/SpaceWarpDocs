Creating Custom Parts
=====================
Disclaimer: This tutorial is for an aspect of modding not fully understood. Most of what we know is sourced by copying 
and pasting information from a very basic part, so going beyond that will have to be up to your own experimentation.

Basic premises
--------------
This tutorial assumes you've read through the :ref:`Addressables Loading` documentation and the :ref:`Translations` documentation.

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

Setting up the part to be addressable
-------------------------------------
Follow all the same steps in the :ref:`Addressables Loading` documentation for making assets addressable, but make sure that the sprites runtime name is :code:`<partName>.png` and the prefabs runtime name is :code:`<partName>.png`


Translation formats for parts
-----------------------------
Without translations, parts will show up as :code:`[TBD]`. So after following the :ref:`Translations` document to create your translations asset, and make sure the following terms of type :code:`Text` are added and filled in
1. :code:`Parts/Title/<part_name>` with the name of the part
2. :code:`Parts/Subtitle/<part_name>` with the subtitle for the part
3. :code:`Parts/Manufacturer/<part_name>` with the manufacturer for the part
4. :code:`Parts/Description/<part_name>` with the description of the part
Example for a custom truss part