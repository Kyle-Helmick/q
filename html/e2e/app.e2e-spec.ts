import { HtmlPage } from './app.po';

describe('html App', function() {
  let page: HtmlPage;

  beforeEach(() => {
    page = new HtmlPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
