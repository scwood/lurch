import commands from '../src/commands';

test('providing number param to list works', async () => {
  const result = await commands.list(75);
  expect(result.split('\n').length).toEqual(78); // +3 for header
});
