from django.db import models

class Kategori(models.Model):
    id_kategori = models.AutoField(primary_key=True)
    nama_kategori = models.CharField(max_length=255)

    def __str__(self):
        return self.nama_kategori

class Kegiatan(models.Model):
    id_kegiatan = models.AutoField(primary_key=True)
    id_kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    nama_kegiatan = models.CharField(max_length=255)
    gambar_kegiatan = models.ImageField(upload_to='static/images/kegiatan')
    deskripsi_kegiatan = models.TextField()

    def __str__(self):
        return self.nama_kegiatan

class GambarKegiatan(models.Model):
    id_gambar = models.AutoField(primary_key=True)
    id_kegiatan = models.ForeignKey(Kegiatan, on_delete=models.CASCADE, related_name='gambar_tambahan')
    gambar = models.ImageField(upload_to='static/images/kegiatan/additional/')
    keterangan = models.CharField(max_length=255, blank=True, null=True)
    urutan = models.PositiveIntegerField(default=1)  # untuk mengurutkan gambar

    class Meta:
        ordering = ['urutan']

    def __str__(self):
        return f"{self.id_kegiatan.nama_kegiatan} - Gambar {self.urutan}"

class Produk(models.Model):
    id_produk = models.AutoField(primary_key=True)
    id_kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    nama_produk = models.CharField(max_length=255)
    nomor_telepon = models.CharField(max_length=20)
    deskripsi_produk = models.TextField()
    gambar_produk = models.ImageField(upload_to='static/images/produk')
    thumbnail_produk = models.ImageField(upload_to='static/images/thumbnails', null=True, blank=True)
    link_shopee = models.URLField("Link Shopee", null=True, blank=True)
    link_tokopedia = models.URLField("Link Tokopedia", null=True, blank=True)
    harga_produk = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nama_produk


class Bundling(models.Model):
    id_bundling = models.AutoField(primary_key=True)
    nama_bundling = models.CharField(max_length=255)
    gambar_bundling = models.ImageField(upload_to='static/images/bundling')
    thumbnail_bundling = models.ImageField(upload_to='static/images/thumbnails', null=True, blank=True)
    harga_bundling = models.DecimalField(max_digits=10, decimal_places=2)
    link_shopee = models.URLField("Link Shopee", null=True, blank=True)
    link_tokopedia = models.URLField("Link Tokopedia", null=True, blank=True)
    deskripsi_bundling = models.TextField()

    def __str__(self):
        return self.nama_bundling

class DetailBundling(models.Model):
    id_db = models.AutoField(primary_key=True)
    id_produk = models.ForeignKey(Produk, on_delete=models.CASCADE)
    id_bundling = models.ForeignKey(Bundling, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id_bundling} - {self.id_produk}"
