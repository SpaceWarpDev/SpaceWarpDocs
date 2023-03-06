SpaceWarp.API.Mods.Mod
======================

Definition
----------

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

Fields
------

::
    
    public BaseModLogger Logger

The mod specific logger, described in the BaseModLogger page ### public
ModInfo info The C# representation of the modinfo.json file for this mod

Methods
-------

::
    
    public virtual void Initialize()

This is called when the mod is first loaded. It is loaded after
dependencies. To extend this make sure to do
``base.Initialize()`` in the subclass :code:`public abstract void
OnInitialized()` This is called after all mods are loaded, this should be
your default entrypoint
