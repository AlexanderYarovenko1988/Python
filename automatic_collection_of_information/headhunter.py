import requests
from bs4 import BeautifulSoup
import fake_useragent
import time
import json

print("Hello!")
def get_links(text):
    ua = fake_useragent.UserAgent()
    data = requests.get(
        url=f"https://hh.ru/search/resume?text={text}&logic=normal&pos=full_text&exp_period=all_time&exp_company_size=any&exp_industry=any&area=113&relocation=living_or_relocation&salary_from=&salary_to=&currency_code=RUR&education=none&age_from=&age_to=&gender=unknown&order_by=relevance&search_period=0&items_on_page=50&no_magic=false&page=1",
        headers={"user-agent": ua.random}
    )
    if data.status_code != 200:
        return
    soup = BeautifulSoup(data.content, "lxml")
    try:
        page_count = int(soup.find("div", attrs={"class": "pager"}).find_all("span", recursive=False)[-1].find("a").find("span").text)
    except:
        return
    for page in range(page_count):
        try:
            data = requests.get(
                url=f"https://hh.ru/search/resume?text={text}&logic=normal&pos=full_text&exp_period=all_time&exp_company_size=any&exp_industry=any&area=113&relocation=living_or_relocation&salary_from=&salary_to=&currency_code=RUR&education=none&age_from=&age_to=&gender=unknown&order_by=relevance&search_period=0&items_on_page=50&no_magic=false&page={page}",
                headers={"user-agent": ua.random}
            )
            if data.status_code != 200:
                continue
            soup = BeautifulSoup(data.content, "lxml")
            for a in soup.find_all("a", attrs={"class": "resume-search-item__name"}):
                yield f"https://hh.ru{a.attrs['href'].split('?')[0]}"
        except Exception as e:
            print(f"{e}")
        time.sleep(1)


def get_resume(link):
    ua = fake_useragent.UserAgent()
    data = requests.get(
        url=link,
        headers={"user-agent": ua.random}
    )
    if data.status_code != 200:
        return
    soup = BeautifulSoup(data.content, "lxml")
    try:
        name = soup.find(attrs={"class": "resume-block__title-text"}).text
    except:
        name = ""
    # try:
    #     salary = soup.find(attrs={"class": "resume-block__title-text_salary"}).text.replace("\u2009", "").replace("\xa0", "")
    # except:
    #     salary = ""
    # try:
    #     tags = [tag.text for tag in soup.find(attrs={"class": "bloko-tag-list"}).find_all(attrs={"class": "bloko-tag__section_text"})]
    # except:
    #     tags = []

    resume = {
        "name": name,
        # "salary": salary,
        # "tags": tags
    }
    return resume


if __name__ == "__main__":
    data = []
    for a in get_links("python"):
        data.append(get_resume(a))
        time.sleep(1)
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)


