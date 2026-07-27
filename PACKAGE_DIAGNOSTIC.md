# Diagnostic du paquet textuel

## Fragments

- `tools/vendor/missing_exercises_text.tar.xz.b64.part-000` : **10000 caractères**
- `tools/vendor/missing_exercises_text.tar.xz.b64.part-001` : **18000 caractères**
- `tools/vendor/missing_exercises_text.tar.xz.b64.part-002` : **18000 caractères**
- `tools/vendor/missing_exercises_text.tar.xz.b64.part-003` : **18000 caractères**
- `tools/vendor/missing_exercises_text.tar.xz.b64.part-004` : **16056 caractères**

- Base64 concaténé : **80056 caractères**
- SHA-256 Base64 : `3f91ea173ee5e22caa6b787b1b4b53ab452f8ff6da69207520d90d28ca63736d`
- Décodage Base64 : **réussi**
- Archive décodée : **60040 octets**
- SHA-256 archive : `9bd5514f9887c10870534e5b07e476a5adb5a7b243ed70c06af1817fcc7fd493`
- Contrôle XZ : **échec**

```text
xz: /tmp/archive.tar.xz: Compressed data is corrupt
```
