import pandas as pd
from bs4 import BeautifulSoup
from mechanize import Browser

def scrapping(url):
    #Handling with bot blocked
    b = Browser()
    b.set_handle_robots(False)
    b.addheaders = [('Referer', 'https://www.reddit.com'), ('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    b.open(url)
    soup = BeautifulSoup(b.response().read(), "html.parser")

    #List infomation:
    result = []

    reviews = soup.find_all('div', class_ = 'a-section review aok-relative')
    for review in reviews:
        list_review = {}
        list_review['name'] = review.find("span", class_ = "a-profile-name").text
        list_review['date'] = review.find("span", class_ = "a-size-base a-color-secondary review-date").text.replace("Reviewed in the United States on ", "")
        list_review['rating'] = review.find("span", class_ = "a-icon-alt").text.replace(" out of 5 stars", "")
        list_review['text'] = review.find("span", class_ = "a-size-base review-text review-text-content").text.replace("\n", "").strip()

        result.append(list_review)
    return result


def main():
    list = []
    list_urls = [
        'https://www.amazon.com/Pepsi-PEPWSC121510752-9541549-WM-KAS/product-reviews/B00OMCXX0Q/ref=cm_cr_getr_d_paging_btm_prev_{}?ie=UTF8&reviewerType=all_reviews&pageNumber={}',
        'https://www.amazon.com/SodaStream%C2%AE-Pepsi%C2%AE-Starry%C2%AE-Beverage-Variety/product-reviews/B0BS9XZ4T4/ref=cm_cr_arp_d_paging_btm_next_{}?ie=UTF8&reviewerType=all_reviews&pageNumber={}',
        'https://www.amazon.com/Coca-Cola-Spiced-7-5oz-10pk/product-reviews/B0CM4GWFDV/ref=cm_cr_arp_d_paging_btm_next_{}?ie=UTF8&reviewerType=all_reviews&pageNumber={}',
        'https://www.amazon.com/Coca-Cola-Spiced-16-9oz-6pk/product-reviews/B0CM4WH5HJ/ref=cm_cr_arp_d_paging_btm_next_{}?ie=UTF8&reviewerType=all_reviews&pageNumber={}',
        'https://www.amazon.com/Coca-Cola-7-5-10-Pack/product-reviews/B06XCMSRM4/ref=cm_cr_arp_d_paging_btm_next_{}?ie=UTF8&reviewerType=all_reviews&pageNumber={}',
        'https://www.amazon.com/Coca-Cola-Zero-Sugar-16-9-Pack/product-reviews/B00FU1YIEI/ref=cm_cr_arp_d_paging_btm_next_{}?ie=UTF8&reviewerType=all_reviews&pageNumber={}',
        'https://www.amazon.com/Coke-Zero-Coca-Cola-Sugar-Pack/product-reviews/B07PGY92MC/ref=cm_cr_arp_d_paging_btm_next_{}?ie=UTF8&reviewerType=all_reviews&pageNumber={}',
        'https://www.amazon.com/Diet-Coke-7-5-10-Pack/product-reviews/B06XCPQPLC/ref=cm_cr_arp_d_paging_btm_next_{}?ie=UTF8&reviewerType=all_reviews&pageNumber={}',
        'https://www.amazon.com/Coke-Diet-Soda-Ounce-Bottles/product-reviews/B000T9UV8S/ref=cm_cr_arp_d_paging_btm_next_{}?ie=UTF8&reviewerType=all_reviews&pageNumber={}'
    ]
    for url in range(0,9,1):
        for i in range(1,15,1):
            url_div = list_urls[url].format(i,i)
            list_of_review = scrapping(url_div)
            list = list + list_of_review
    df = pd.DataFrame(list)
    df.to_csv("data_final.csv", encoding='utf-8-sig')

if __name__ == "__main__":
    main()

#https://www.amazon.com/Pepsi-PEPWSC121510752-9541549-WM-KAS/product-reviews/B00OMCXX0Q/ref=cm_cr_getr_d_paging_btm_prev_{}?ie=UTF8&reviewerType=all_reviews&pageNumber={}
#https://www.amazon.com/SodaStream%C2%AE-Pepsi%C2%AE-Starry%C2%AE-Beverage-Variety/product-reviews/B0BS9XZ4T4/ref=cm_cr_arp_d_paging_btm_next_{}?ie=UTF8&reviewerType=all_reviews&pageNumber={}
#https://www.amazon.com/Coca-Cola-Spiced-7-5oz-10pk/product-reviews/B0CM4GWFDV/ref=cm_cr_arp_d_paging_btm_next_{}?ie=UTF8&reviewerType=all_reviews&pageNumber={}
#https://www.amazon.com/Coca-Cola-Spiced-16-9oz-6pk/product-reviews/B0CM4WH5HJ/ref=cm_cr_arp_d_paging_btm_next_{}?ie=UTF8&reviewerType=all_reviews&pageNumber={}
#https://www.amazon.com/Coca-Cola-7-5-10-Pack/product-reviews/B06XCMSRM4/ref=cm_cr_arp_d_paging_btm_next_{}?ie=UTF8&reviewerType=all_reviews&pageNumber={}
#https://www.amazon.com/Coca-Cola-Zero-Sugar-16-9-Pack/product-reviews/B00FU1YIEI/ref=cm_cr_arp_d_paging_btm_next_{}?ie=UTF8&reviewerType=all_reviews&pageNumber={}
#https://www.amazon.com/Coke-Zero-Coca-Cola-Sugar-Pack/product-reviews/B07PGY92MC/ref=cm_cr_arp_d_paging_btm_next_{}?ie=UTF8&reviewerType=all_reviews&pageNumber={}
#https://www.amazon.com/Diet-Coke-7-5-10-Pack/product-reviews/B06XCPQPLC/ref=cm_cr_arp_d_paging_btm_next_{}?ie=UTF8&reviewerType=all_reviews&pageNumber={}
#https://www.amazon.com/Coke-Diet-Soda-Ounce-Bottles/product-reviews/B000T9UV8S/ref=cm_cr_arp_d_paging_btm_next_{}?ie=UTF8&reviewerType=all_reviews&pageNumber={}