const handleExpirationDate = (action) => {
  // Get the corresponding action and messages
  const refs = handleConstants(action);

  const blueGroupName = document.getElementById(
    'expiration-date-tab-bluegroup-name-text-input'
  );

  const expirationDatePicker = document.getElementById(
    'expiration-date-date-picker-input'
  );
  const expirationDate = new Date(expirationDatePicker.value);
  const expirationDay = expirationDate.getUTCDate();
  const expirationMonth = expirationDate.getUTCMonth() + 1;
  const expirationYear = expirationDate.getUTCFullYear();

  const expirationDateToggle = document.getElementById(
    'expiration-date-tab-toggle'
  );
  const w3Email = document.getElementById('w3-email-text-input');
  const w3Password = document.getElementById('w3-password-text-input');

  handleRequest({
    url: '/expiration_date',
    method: 'POST',
    data: {
      action: refs.action,
      blueGroupName: blueGroupName.value,
      expirationDay: expirationDay,
      expirationMonth: expirationMonth,
      expirationYear: expirationYear,
      expirationDateToggle: expirationDateToggle.checked,
      w3Email: w3Email.value,
      w3Password: w3Password.value,
    },
    successCallback: () => displayModal(true, refs.messages.SUCCESS),
    errorCallback: () => displayModal(false, refs.messages.ERROR),
    clickedButtonRef: refs.action,
  });
};
