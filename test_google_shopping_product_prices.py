import unittest
import google_shopping_product_prices as gs


def PULVERIZADOR_MATABI_PRODUCT_URL():
    return "https://www.google.es/search?hl=es" \
           "&tbm=shop" \
           "&sxsrf=ALeKk00NkGAPStnPSrndUwZSdcuj3U8XlA%3A1590854655004" \
           "&ei=_oPSXtXsPIryapv3mLgE" \
           "&q=pulverizador+matabi+evolution+15+ltc" \
           "&oq=pulverizador+matabi+evolution+15+ltc" \
           "&gs_l=psy-ab-sh.12...0.0.0.5796.0.0.0.0.0.0.0.0..0.0....0...1c..64.psy-ab-sh..0.0.0....0.kXcJGJ9uh4k"


def RUBI_CORTADORA_PRODUCT_URL():
    return "https://www.google.com/search?rlz=1C5CHFA_enES783ES783" \
           "&biw=1920" \
           "&bih=946" \
           "&tbm=shop" \
           "&sxsrf=ALeKk02F6aITmb62zyuaGb1kSiE3Um1KHg%3A1597136122298" \
           "&ei=-lwyX-fZEdKIjLsPhYKR2A0" \
           "&q=rubi+tz+1300" \
           "&oq=rubi+tz+1300" \
           "&gs_lcp=Cgtwcm9kdWN0cy1jYxADMgQIIxAnMgIIADIECAAQGDIGCAAQBRAeMgYIABAFEB4yBggAEAgQHjoECAAQHlClpXRYpaV0YNiqdGgAcAB4AIABXogBtgGSAQEymAEAoAECoAEBqgEPcHJvZHVjdHMtY2Mtd2l6wAEB" \
           "&sclient=products-cc" \
           "&ved=0ahUKEwjnvujZ45LrAhVSBGMBHQVBBNsQ4dUDCAo" \
           "&uact=5"


class TestPricePrinter(unittest.TestCase):

    def test_retrieve_google_shopping_prices_pulverizador_matabi(self):
        result = gs.retrieve_google_shopping_prices(PULVERIZADOR_MATABI_PRODUCT_URL(), "HRLxBb")
        self.assertTrue(len(result) > 0)

    def test_retrieve_google_shopping_prices_rubi_cortadora(self):
        result = gs.retrieve_google_shopping_prices(RUBI_CORTADORA_PRODUCT_URL(), "HRLxBb")
        self.assertTrue(len(result) > 0)


if __name__ == '__main__':
    unittest.main()
