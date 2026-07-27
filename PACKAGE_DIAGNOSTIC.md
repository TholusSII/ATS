# Diagnostic du paquet textuel

## Fragments

- `tools/vendor/missing_exercises_text.tar.xz.b64.part-000` : **10000 caractères**
- `tools/vendor/missing_exercises_text.tar.xz.b64.part-000a` : **18000 caractères**
- `tools/vendor/missing_exercises_text.tar.xz.b64.part-001` : **18000 caractères**
- `tools/vendor/missing_exercises_text.tar.xz.b64.part-002` : **18000 caractères**
- `tools/vendor/missing_exercises_text.tar.xz.b64.part-003` : **18000 caractères**
- `tools/vendor/missing_exercises_text.tar.xz.b64.part-004` : **16056 caractères**

- Base64 concaténé : **98056 caractères**
- SHA-256 Base64 : `3c0f7fb2025372435f9c1850e95a124b8d81cba50d61a55cec29059506fe2660`
- Décodage Base64 : **réussi**
- Archive décodée : **73540 octets**
- SHA-256 archive : `99a8f6b4f46d9a8ea81792d72ebbab90e225046787ac4ce1ae12bef8ee8b7cab`
- Contrôle XZ : **échec**

```text
xz: /tmp/archive.tar.xz: Compressed data is corrupt
```
