const handleOwner = (action) => {
  // Get the corresponding action and messages
  const refs = handleConstants(action);

  const blueGroupName = document.getElementById(
    'owner-tab-bluegroup-name-text-input'
  );
  const ownerToggle = document.getElementById('owner-tab-toggle');
  const userId = document.getElementById('owner-tab-uid-text-input');
  const w3Email = document.getElementById('w3-email-text-input');
  const w3Password = document.getElementById('w3-password-text-input');

  handleRequest({
    url: '/owner',
    method: 'POST',
    data: {
      action: refs.action,
      blueGroupName: blueGroupName.value,
      ownerToggle: ownerToggle.checked,
      userId: userId.value,
      w3Email: w3Email.value,
      w3Password: w3Password.value,
    },
    successCallback: () => displayModal(true, refs.messages.SUCCESS),
    errorCallback: () => displayModal(false, refs.messages.ERROR),
    clickedButtonRef: refs.action,
  });
};
