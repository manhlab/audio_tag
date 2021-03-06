sample_rate = 32000
clip_samples = sample_rate * 30

mel_bins = 64
fmin = 50
fmax = 14000
window_size = 1024
hop_size = 320
window = 'hann'
pad_mode = 'reflect'
center = True
device = 'cuda'
ref = 1.0
amin = 1e-10
top_db = None

labels = ['aldfly', 'ameavo', 'amebit', 'amecro', 'amegfi', 'amekes',
       'amepip', 'amered', 'amerob', 'amewig', 'amewoo', 'amtspa',
       'annhum', 'astfly', 'baisan', 'baleag', 'balori', 'banswa',
       'barswa', 'bawwar', 'belkin1', 'belspa2', 'bewwre', 'bkbcuc',
       'bkbmag1', 'bkbwar', 'bkcchi', 'bkchum', 'bkhgro', 'bkpwar',
       'bktspa', 'blkpho', 'blugrb1', 'blujay', 'bnhcow', 'boboli',
       'bongul', 'brdowl', 'brebla', 'brespa', 'brncre', 'brnthr',
       'brthum', 'brwhaw', 'btbwar', 'btnwar', 'btywar', 'buffle',
       'buggna', 'buhvir', 'bulori', 'bushti', 'buwtea', 'buwwar',
       'cacwre', 'calgul', 'calqua', 'camwar', 'cangoo', 'canwar',
       'canwre', 'carwre', 'casfin', 'caster1', 'casvir', 'cedwax',
       'chispa', 'chiswi', 'chswar', 'chukar', 'clanut', 'cliswa',
       'comgol', 'comgra', 'comloo', 'commer', 'comnig', 'comrav',
       'comred', 'comter', 'comyel', 'coohaw', 'coshum', 'cowscj1',
       'daejun', 'doccor', 'dowwoo', 'dusfly', 'eargre', 'easblu',
       'easkin', 'easmea', 'easpho', 'eastow', 'eawpew', 'eucdov',
       'eursta', 'evegro', 'fiespa', 'fiscro', 'foxspa', 'gadwal',
       'gcrfin', 'gnttow', 'gnwtea', 'gockin', 'gocspa', 'goleag',
       'grbher3', 'grcfly', 'greegr', 'greroa', 'greyel', 'grhowl',
       'grnher', 'grtgra', 'grycat', 'gryfly', 'haiwoo', 'hamfly',
       'hergul', 'herthr', 'hoomer', 'hoowar', 'horgre', 'horlar',
       'houfin', 'houspa', 'houwre', 'indbun', 'juntit1', 'killde',
       'labwoo', 'larspa', 'lazbun', 'leabit', 'leafly', 'leasan',
       'lecthr', 'lesgol', 'lesnig', 'lesyel', 'lewwoo', 'linspa',
       'lobcur', 'lobdow', 'logshr', 'lotduc', 'louwat', 'macwar',
       'magwar', 'mallar3', 'marwre', 'merlin', 'moublu', 'mouchi',
       'moudov', 'norcar', 'norfli', 'norhar2', 'normoc', 'norpar',
       'norpin', 'norsho', 'norwat', 'nrwswa', 'nutwoo', 'olsfly',
       'orcwar', 'osprey', 'ovenbi1', 'palwar', 'pasfly', 'pecsan',
       'perfal', 'phaino', 'pibgre', 'pilwoo', 'pingro', 'pinjay',
       'pinsis', 'pinwar', 'plsvir', 'prawar', 'purfin', 'pygnut',
       'rebmer', 'rebnut', 'rebsap', 'rebwoo', 'redcro', 'redhea',
       'reevir1', 'renpha', 'reshaw', 'rethaw', 'rewbla', 'ribgul',
       'rinduc', 'robgro', 'rocpig', 'rocwre', 'rthhum', 'ruckin',
       'rudduc', 'rufgro', 'rufhum', 'rusbla', 'sagspa1', 'sagthr',
       'savspa', 'saypho', 'scatan', 'scoori', 'semplo', 'semsan',
       'sheowl', 'shshaw', 'snobun', 'snogoo', 'solsan', 'sonspa', 'sora',
       'sposan', 'spotow', 'stejay', 'swahaw', 'swaspa', 'swathr',
       'treswa', 'truswa', 'tuftit', 'tunswa', 'veery', 'vesspa',
       'vigswa', 'warvir', 'wesblu', 'wesgre', 'weskin', 'wesmea',
       'wessan', 'westan', 'wewpew', 'whbnut', 'whcspa', 'whfibi',
       'whtspa', 'whtswi', 'wilfly', 'wilsni1', 'wiltur', 'winwre3',
       'wlswar', 'wooduc', 'wooscj2', 'woothr', 'y00475', 'yebfly',
       'yebsap', 'yehbla', 'yelwar', 'yerwar', 'yetvir']
    
lb_to_idx = {lb: idx for idx, lb in enumerate(labels)}
idx_to_lb = {idx: lb for idx, lb in enumerate(labels)}
classes_num = len(labels)