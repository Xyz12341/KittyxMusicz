if (chat.chat_type != "private") {
  if (data.message == "/lock") {
    Api.setChatPermissions({
      chat_id: request.chat.id,
      permissions: JSON.stringify({ can_send_messages: false })
    })
    Api.sendMessage({
      text: "Locked!",
      parse_mode: "Markdown",
      reply_to_message_id: request.message_id
    })
    return
  }
  if (data.message == "/unlock") {
    Api.setChatPermissions({
      chat_id: request.chat.id,
      permissions: JSON.stringify({ can_send_messages: true })
    })
    Api.sendMessage({
      text: "Unocked!",
      parse_mode: "Markdown",
      reply_to_message_id: request.message_id
    })
    return
  }
  return
}
