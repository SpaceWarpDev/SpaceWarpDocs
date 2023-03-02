Конфигурация
==============

Создание класса конфигурации
------------------------------

.. code:: cs

   using SpaceWarp.API.Configuration;
   using Newtonsoft.Json;
   namespace Namespace;
   [JsonObject(MemberSerialization.OptOut)]
   [ModConfig]
   public class Config {
      ...
   }

Поля конфигурации
-----------------

Чтобы создать новое поле, сделайте следующее (это создаст поле ввода/переключения).
поле в редакторе конфигов в Space Warp)

.. code:: cs

   [ConfigField("name")]
   [ConfigDefaultValue(3)] // Optional
   public int name;

Разделы конфигурации
--------------------
.. code:: cs

   [ConfigSection("folder/in/menu")]
   [ConfigField("name")]
   ...

Получение конфигурации из вашего мода
---------------------------------------

.. code:: cs

   using SpaceWarp.API.Configuration;
   .
   .
   .
   ManagerLocator.TryGet(out ConfigurationManager configManager);
   Config conf = null; //Config is the name of your configuration class
   if (configManager.TryGet("mod_id",out var config)) conf = (Config)conf.configObject;
