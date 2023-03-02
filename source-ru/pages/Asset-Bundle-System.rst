Система загрузки пакетов активов
============================

Начиная с версии 0.2.0, Space Warp предоставляет загрузчик пакетов ресурсов, который загружает и кэширует все ресурсы в разделе «SpaceWarp/assets/bundles» для внутренних ресурсов Space Warp и «ModFolder/assets/bundles».

Пакеты ресурсов должны иметь расширение .bundle.

Импорт
-------

::

    используя SpaceWarp.API.AssetBundles

Методы
-------

**public static T ResourceManager.GetAsset<T>(string path) where T : UnityEngine.Object**

Это загружает актив из пути и бросает, если он не может

**public static bool ResourceManager.TryGet<T>(string path, out T asset) where T : UnityEngine.Object**

Это загружает актив из пути и возвращает true в случае успеха, в противном случае он возвращает false и устанавливает для актива значение null.

Пути
-----

Пути имеют следующий формат:

- `[mod_id]/[название бандла без .bundle]/[путь к ассету в бандле без ассетов/]`
- Для внутренних ассетов Space Warp: `space_warp/[название бандла без .bundle]/[путь к ассету в бандле без ассетов/]/`