describe('Test Home', () => {
  it('You can add a new todo', () => {
    cy.visit('http://localhost:3000')
    const todoTitle = 'Buy groceries'

    cy.get('[data-testid="add-todo"]').click()
    cy.get('[data-testid="todo-modal"]').should('exist')


    cy.get('input[name="title"]').type(todoTitle);
    cy.get('input[name="description"]').type('This is a new todo item');

    // Click on the "Save" button
    cy.contains('Save').click();

    cy.contains('li', todoTitle)
  })
})