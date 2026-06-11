describe('Checkbox Tests', () => {
  it('should have correct initial checkbox states', () => {
    cy.visit('https://the-internet.herokuapp.com/checkboxes')
    cy.get('input[type="checkbox"]').eq(0).should('not.be.checked')
    cy.get('input[type="checkbox"]').eq(1).should('be.checked')
  })

  it('should be able to check checkbox 1', () => {
    cy.visit('https://the-internet.herokuapp.com/checkboxes')
    cy.get('input[type="checkbox"]').eq(0).check()
    cy.get('input[type="checkbox"]').eq(0).should('be.checked')
  })
})
