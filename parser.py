import tabula, json, os, datetime, hashlib

scriptDir = os.path.dirname(os.path.abspath(__file__))

def parseRaw(src):
    df = tabula.read_pdf(src, output_format="json", pages='all')
    
    master = []

    for page in df:
        rows = page['data']
        page_data = []
        
        for row in rows:
            res = []
            for data in row:
                res.append(data['text'])
            master.append(res)
        
    return master

def getMasterJadwal(raw):
    jadwal = []
    hari=tgl=waktu=matkul=dosen=''
    temp_tgl = ''

    for row in raw:
        if row[0] != 'HARI':
            try:
                if row[3]:
                    hari = row[0]
                    tgl = row[1]
                    matkul = row[2]
                    waktu = row[3]
                    dosen = row[4]
                else:
                    hari = row[0]
                    tgl = row[1]
                    matkul = row[2]
                    waktu = row[4]
                    dosen = row[5]

                if not matkul:
                    matkul = 'Libur'
            except:
                print(temp_tgl, row)

            temp_tgl=tgl

            data = {
                'hari': hari,
                'tanggal': tgl,
                'matkul': matkul,
                'jam': waktu,
                'dosen': dosen
            }
            jadwal.append(data)

    return jadwal

def getSpecificJadwal(jadwal_master):
    jadwal_harian = []

    for jadwal in jadwal_master:
        print(jadwal)
        

# def saveJadwalToJSON():
#     if not os.path.exists(scriptDir+'/Jadwal/'):
#         os.makedirs(scriptDir+'/Jadwal/')

#     with open('Jadwal/jadwalHarian.json', 'w') as fp:
#         json.dump(jadwal_harian, fp, indent=2)
#     # with open('Jadwal/jadwalLiburan.json', 'w') as fp:
#     #     json.dump(liburan, fp, indent=2)


raw = parseRaw('jadwalBaru.pdf')
jadwal_master = getMasterJadwal(raw)
# print(getSpecificJadwal(jadwal_master))



# print(scriptDir)

# print(json.dumps(jadwal_harian, indent=2))
# print(json.dumps(liburan, indent=2))