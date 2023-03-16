Translations
============

Setup
-----
Follow all the setup in the :ref:`Addressables Loading` documentation. Make sure the addressables labels for your bundle contains `language_source`

Creation of a localization
--------------------------

1. Create an asset of type :code:`LanguageSourceAsset`.
2. Then add all the languages you want to have the asset in under the `M Languages` property
3. Then add all the terms you need in `M Terms`
4. Then for each term choose the correct type, make sure the term is the correct type, then fill in the languages in the order that you added the languages under `M Languages`
5. Then make sure this asset is addressable.
