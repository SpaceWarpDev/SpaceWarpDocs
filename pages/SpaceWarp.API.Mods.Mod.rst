SpaceWarp.API.Mods.Mod
======================

Определение
-----------

.. code:: cs

   public abstract class Mod : KerbalMonobehaviour
   {
       public BaseModLogger Logger;
       public ModInfo info;
       public virtual void Initialize()
       {
           ModLocator.Add(this);
           DontDestroyOnLoad(gameObject);
       }
       public abstract void OnInitialized();
   }

Поля
----

public BaseModLogger Logger
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Регистратор для конкретного мода, описанный на странице BaseModLogger ### public
Информация о ModInfo C#-представление файла modinfo.json для этого мода.

Методы
-------

public virtual void Initialize()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Вызывается при первой загрузке мода, загружается после
зависимости на данный момент, чтобы расширить это, обязательно сделайте
``base.Initialize()`` в подклассе ### public abstract void
OnInitialized() Вызывается после загрузки всех модов, это должно быть
ваша точка входа по умолчанию
