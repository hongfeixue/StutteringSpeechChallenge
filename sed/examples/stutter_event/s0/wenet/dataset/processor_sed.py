def sed_label(data):
    """ Decode text to chars or BPE
        Inplace operation

        Args:
            data: Iterable[{key, wav, txt, sample_rate}]

        Returns:
            Iterable[{key, wav, txt, label, sample_rate}]
    """
    for sample in data:
        assert 'txt' in sample
        txt = sample['txt'].strip()
        sample['label'] = [int(l) for l in txt.split(',')]
        yield sample