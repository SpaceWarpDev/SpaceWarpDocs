Configuration
=============

Creating a Configuration Class
------------------------------

.. code:: cs

   using SpaceWarp.API.Configuration;
   using Newtonsoft.Json;
   namespace Namespace;
   [JsonObject(MemberSerialization.OptOut)]
   [ModConfig]
   public class Config 
   {
      ...
   }

Configuration Fields
--------------------

In order to create a new field in the configuration menu, add the following. 

(this creates an input/toggle field in the config editor in Space Warp)

.. code:: cs

   [ConfigField("name")]
   [ConfigDefaultValue(3)] // Optional
   public int name;

Configuration Sections
----------------------

.. code:: cs

   [ConfigSection("folder/in/menu")]
   [ConfigField("name")]
   ...

Getting The Configuration From Your Mod
---------------------------------------

.. code:: cs

   using SpaceWarp.API.Configuration;
   .
   .
   .
   ManagerLocator.TryGet(out ConfigurationManager configManager);
   Config conf = null; //Config is the name of your configuration class
   if (configManager.TryGet("mod_id",out var config)) conf = (Config)conf.configObject;
