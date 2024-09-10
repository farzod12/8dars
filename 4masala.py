def fayllarni_ko

  try:
    with open(manba_fayli, 'r') as manba:
      with open(maqsad_fayli, 'w') as maqsad:
        maqsad.write(manba.read())
    print(f"{manba_fayli} fayli {maqsad_fayli} fayliga muvaffaqiyatli ko'chirildi.")
  except FileNotFoundError:
    print(f"{manba_fayli} fayli topilmadi.")
  except Exception as e:
    print(f"Xatolik yuz berdi: {e}")



