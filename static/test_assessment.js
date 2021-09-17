'use strict';

// These are our custom matchers. They make the test report look pretty.
// Keep scrolling for the actual tests!
const customMatchers = {
  htmlContentsToBe: (matchUtils) => {
    return {
      compare: (actual, expected) => {
        const result = {};

        const htmlContent = actual.outerHTML;
        result.pass = matchUtils.equals(
          htmlContent.replaceAll(/\s+/g, ''),
          expected.replaceAll(/\s+/g, '')
        );
        if (result.pass) {
          result.message = `Expected the resulting HTML:\n\n${expected}`;
        } else {
          result.message = `Expected the resulting HTML:\n\n${expected}\n\n...but instead got:\n\n${htmlContent}`;
        }

        return result;
      },
    };
  },
  fontColorToBe: (matchUtils) => {
    return {
      compare: (actual, expected) => {
        const result = {};

        const actualColor = actual.style.color;
        result.pass = matchUtils.equals(actualColor, expected);

        if (result.pass) {
          result.message = `Expected font color of ${actual.outerHTML} to be ${expected}.`;
        } else {
          result.message = `Expected font color of ${actual.outerHTML} to be ${expected} but instead it was ${actual.style.color}.`;
        }

        return result;
      },
    };
  },
};

const setup = () => {
  jasmine.addMatchers(customMatchers);
};

// More setup before tests run.
(() => {
  const env = jasmine.getEnv();
  env.configure({ random: false });

  // We should probably consider intercepting requests that happen by default when
  // forms are submitted. We need to do this to prevent errant form submissions from requesting
  // this page again, which re-runs the tests, which request this page again, causing you to
  // be stuck in an infinite loop.
  document.querySelectorAll('form').forEach((form) => {
    form.addEventListener('submit', (evt) => {
      evt.preventDefault();
      evt.stopPropagation();
    });
  });
})();

// Actual tests start below
describe('Prompt #1', () => {
  beforeEach(setup);

  const button = document.querySelector('#prompt-1 button');

  it('When the button says "Log In", clicking on it should make the button say "Log Out"', () => {
    button.innerText = 'Log In';
    button.click();

    expect(button).htmlContentsToBe('<button id="login-button">Log Out</button>');
  });

  it('When the button says "Log Out", clicking on it should make the button say "Log In"', () => {
    button.innerText = 'Log Out';
    button.click();

    expect(button).htmlContentsToBe('<button id="login-button">Log In</button>');
  });
});

describe('Prompt #2', () => {
  const form = document.querySelector('#prompt-2 form');
  const button = form.querySelector('button');

  it('Clicking on the "Send Alert!" button should cause an alert to appear', () => {
    const alertspy = spyOn(window, 'alert');

    button.click();

    expect(alertspy).toHaveBeenCalled();
  });

  it('The alert message can be customized by the user.', () => {
    const alertspy = spyOn(window, 'alert');

    document.querySelector('#alert-text').value = 'TEST';
    button.click();

    expect(alertspy).toHaveBeenCalledWith('TEST');
  });
});

describe('Prompt #3', () => {
  beforeEach(setup);

  const button = document.querySelector('#prompt-3 button');
  const list = document.querySelector('#prompt-3 ul');

  it('Clicking the button should add a list item.', () => {
    button.click();

    expect(list).htmlContentsToBe(`
      <ul id="list">
        <li>Item</li>
        <li>Item</li>
      </ul>
    `);
  });
});

describe('Prompt #4', () => {
  beforeEach(setup);

  const prompt = document.querySelector('#prompt-4');
  const redButton = document.querySelector('#prompt-4 button[id*="red"]');
  const blueButton = document.querySelector('#prompt-4 button[id*="blue"]');

  it('"Turn Stuff Red" should turn elements with .changes-colors red', () => {
    redButton.click();

    let currChild = prompt.firstElementChild;
    while (currChild) {
      if (currChild.classList.contains('changes-colors')) {
        expect(currChild).fontColorToBe('red');
      } else {
        expect(currChild).fontColorToBe('');
      }

      currChild = currChild.nextElementSibling;
    }
  });

  it('"Turn Stuff Blue" should turn elements with .changes-colors blue', () => {
    blueButton.click();

    let currChild = prompt.firstElementChild;
    while (currChild) {
      if (currChild.classList.contains('changes-colors')) {
        expect(currChild).fontColorToBe('blue');
      } else {
        expect(currChild).fontColorToBe('');
      }

      currChild = currChild.nextElementSibling;
    }
  });
});

describe('Prompt #5', () => {
  beforeEach(setup);

  let berriesList = document.querySelector('#prompt-5 ol');

  it('List should display names of berries from Pokemon API', () => {
    berriesList.expect;
    expect(berriesList).htmlContentsToBe(`
      <ol id="berries">
        <li>cheri</li>
        <li>chesto</li>
        <li>pecha</li>
        <li>rawst</li>
        <li>aspear</li>
        <li>leppa</li>
        <li>oran</li>
        <li>persim</li>
        <li>lum</li>
        <li>sitrus</li>
        <li>figy</li>
        <li>wiki</li>
        <li>mago</li>
        <li>aguav</li>
        <li>iapapa</li>
        <li>razz</li>
        <li>bluk</li>
        <li>nanab</li>
        <li>wepear</li>
        <li>pinap</li>
      </ol>
    `);
  });
});

describe('Prompt #6', () => {
  beforeEach(setup);

  const form = document.querySelector('#prompt-6 form');
  const submitBtn = form.querySelector('input[type="submit"]');

  it('Should be able to calculate 6! (6 * 5 * 4 * 3 * 2 * 1) and display the result (720).', () => {
    form.querySelector('input[type="number"]').value = '6';
    form.requestSubmit();

    expect(form.nextElementSibling).htmlContentsToBe(
      '<p>Result of calculation: <span id="factorial-result">720</span></p>'
    );
  });
});
