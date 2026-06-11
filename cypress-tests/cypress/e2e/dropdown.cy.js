describe('Dropdown Tests', () => {
  it('should select Option 1', () => {
    cy.visit('https://the-internet.herokuapp.com/dropdown')
    cy.get('#dropdown').select('Option 1')
    cy.get('#dropdown').should('have.value', '1')
  })

  it('should select Option 2', () => {
    cy.visit('https://the-internet.herokuapp.com/dropdown')
    cy.get('#dropdown').select('Option 2')
    cy.get('#dropdown').should('have.value', '2')
  })
})
