def includeme(config):
    # Process settings to remove storage wording.
    settings = config.get_settings()

    storage_settings = {}
    for k, v in settings.items():
        if k.startswith('attachment.'):
            k = k.replace('attachment.', 'storage.')
            storage_settings[k] = v

    # Force some pyramid_storage settings.
    storage_settings['storage.name'] = 'attachment'

    config.add_settings(storage_settings)

    if 'storage.base_path' in storage_settings:
        config.include('pyramid_storage.local')
    else:
        config.include('pyramid_storage.s3')

    config.scan('kinto_attachment.views')
