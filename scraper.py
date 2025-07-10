import requests
from bs4 import BeautifulSoup

BASE_URL = "https://huggingface.co"
PAPERS_URL = f"{BASE_URL}/papers"

def scrape_papers():
    """
    Hugging Face Daily Papers 페이지에서 최신 논문 목록을 스크래핑합니다.

    Returns:
        list: 논문 정보를 담은 딕셔너리 리스트. 각 딕셔너리에는 'title'과 'url'이 포함됩니다.
              예: [{'title': 'Paper Title', 'url': 'https://huggingface.co/papers/...'}]
    """
    try:
        response = requests.get(PAPERS_URL)
        response.raise_for_status()  # HTTP 에러가 발생하면 예외를 발생시킵니다.
    except requests.exceptions.RequestException as e:
        print(f"Error fetching papers: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    papers = []
    
    # 1. 메인 콘텐츠 영역을 먼저 찾습니다.
    main_content = soup.find('main')
    if not main_content:
        print("Error: Could not find the main content area of the page. The website structure might have changed.")
        return []

    # 2. 메인 콘텐츠 내에서 모든 article 태그를 찾습니다.
    paper_articles = main_content.find_all('article')
    if not paper_articles:
        print("No articles found within the main content. The website structure might have changed.")
        return []

    # 3. 각 article에서 논문 정보를 추출합니다.
    for article in paper_articles:
        # h3 태그를 먼저 찾습니다.
        h3_tag = article.find('h3')
        if h3_tag:
            # h3 태그 안의 a 태그에서 제목과 링크를 찾습니다.
            link_tag = h3_tag.find('a')
            if link_tag and link_tag.has_attr('href'):
                title = link_tag.get_text(strip=True)
                relative_url = link_tag['href']
                full_url = f"{BASE_URL}{relative_url}"
                papers.append({'title': title, 'url': full_url})
            
    return papers

if __name__ == '__main__':
    # 스크래퍼 단독 실행 테스트
    latest_papers = scrape_papers()
    if latest_papers:
        print(f"Found {len(latest_papers)} papers:")
        for paper in latest_papers:
            print(f"- {paper['title']}: {paper['url']}")
    else:
        print("Could not retrieve papers.")
