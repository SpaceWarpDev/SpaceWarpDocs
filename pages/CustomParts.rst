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

Using the new Colors feature
----------------------------
KSP 2 has a new feature allowing for parts to be colored in the VAB. But we can't directly set this up in Unity since KSP 2 uses a
custom shader. SpaceWarp has an alternative to this.

First, in Unity, set all the materials on your part that are meant to be replaced to `Standard` (Unity built in shader),
then, in your `ModPlugin` class (in either :code:`OnPreInitialized` or :code:`OnInitialized`) call :code:`Colors.DeclareParts`.
See below for an example:

.. code-block:: c#

    using SpaceWarp.API.Parts;
    
    ...
    
    OnPreInitialized()
    {
        Colors.DeclareParts(MyPluginInfo.PLUGIN_GUID, "truss_2v_square_1x1_custom", "truss_2v_square_1x2_custom", "truss_2v_square_1x4_custom");
    }

Or you can pass an IEnumerable of strings:

.. code-block:: c#

    using SpaceWarp.API.Parts;

    ...

    List<string> myParts = new List<string>()
    {
        "truss_2v_square_1x1_custom",
        "truss_2v_square_1x2_custom",
        "truss_2v_square_1x4_custom"
    };

    OnPreInitialized()
    {
        Colors.DeclareParts(MyPluginInfo.PLUGIN_GUID, myParts);
    }

Now, in your mod directory, create an :code:`images` folder inside the :code:`assets` folder, then add your textures in the format
:code:`<partName><textureMapType>.png`, where :code:`<partName>` is the name of your part from the config JSON and :code:`<textureMapType>`
is an abbreviation of the texture: :code:`_d` for diffuse, :code:`_n` for normal, :code:`_m` for mettalic, :code:`_ao` for ambient occlusion, 
:code:`_e` for emission and :code:`_pm` for paint map. All textures must be in the PNG format.

You only need the diffuse texture and the paint map texture for the color feature to work, but if you have other textures feel free to
add them, see below for an example:

::
    ExampleMod
    |
    \-- assets
        |
        \-- images
            |
            +-- truss_2v_square_1x1_custom
            |   |
            |   +--truss_2v_square_1x1_custom_d.png
            |   +--truss_2v_square_1x1_custom_n.png
            |   +--truss_2v_square_1x1_custom_m.png
            |   +--truss_2v_square_1x1_custom_ao.png
            |   +--truss_2v_square_1x1_custom_e.png
            |   +--truss_2v_square_1x1_custom_pm.png
            |
            +-- truss_2v_square_1x2_custom
                |
                +-- truss_2v_square_1x2_custom_d.png
                +-- truss_2v_square_1x2_custom_pm.png


If for some reason your part's colors aren't getting changed, you can check the logs for more information, all color
related logs are after :code:`TTR` (short for Taste The Rainbow).

Translation formats for parts
-----------------------------
Without translations, parts will show up as :code:`[TBD]`. So after following the :ref:`Translations` document to create your translations asset, and make sure the following terms of type :code:`Text` are added and filled in
1. :code:`Parts/Title/<part_name>` with the name of the part
2. :code:`Parts/Subtitle/<part_name>` with the subtitle for the part
3. :code:`Parts/Manufacturer/<part_name>` with the manufacturer for the part
4. :code:`Parts/Description/<part_name>` with the description of the part
Example for a custom truss part
