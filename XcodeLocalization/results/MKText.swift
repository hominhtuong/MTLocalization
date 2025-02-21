//
//  MKText.swift
//
        
import UIKit
        
enum MKText: String {
        
   case general_appName
   case tabbar_calculator
   case tabbar_weighing
   case tabbar_settings
   case screen_weighing_summary
   case screen_weighing_export
   case screen_weighing_defective
   case screen_weighing_bulk
   case language_selectLanguage
   case language_arabic
   case language_ukrainian
   case language_turkish
   case language_thai
   case language_spanish
   case language_russian
   case language_portuguese
   case language_polish
   case language_latvian
   case language_lao
   case language_malay
   case language_korean
   case language_khmer
   case language_kannada
   case language_japanese
   case language_italian
   case language_indonesian
   case language_hindi
   case language_greek
   case language_german
   case language_french
   case language_finnish
   case language_estonian
   case language_dutch
   case language_czech
   case language_chinese
   case language_english
   case language_vietnamese
   case language_languages
   case ads_Unlimited
   case ads_Advertisements
   case ads_NoAds
   case register_agreeTerms
   case settings_actions_restorePurchase
   case settings_actions_feedback
   case settings_actions_shareApp
   case settings_actions_rateAndReview
   case settings_actions_term
   case settings_actions_policy
   case settings_theme_textColor
   case settings_theme_backgroundColor
   case settings_theme_boxColor
   case actions_selectAll
   case actions_deselectAll
   case actions_cancel
   case actions_done
   case actions_send
   case actions_ok
   case actions_edit
   case actions_select
   case actions_selected
   case actions_delete
   case actions_share
   case actions_completed
   case actions_error
   case actions_search
   case actions_version
   case general_loading
   case general_noInternetMessage
   case actions_retry
   case general_txt_rate
   case actions_txt_give_5_stars
   case actions_txt_no_thanks
   case actions_txt_notice
   case inapp_get_7_days_for_free
   case inapp_super_promotion
   case inapp_get_3_days_for_free
   case inapp_weekly_premium
   case inapp_monthly_premium
   case inapp_yearly_premium
   case inapp_weekly_premium_sale_off
   case general_crate
   case general_delete_sheet_title
   case general_delete_sheet_message
   case general_create_record
   case general_edit_record
   case general_at
   case general_buy_in
   case general_sell_out
   case general_customer_name
   case general_phone
   case general_address
   case general_note
   case general_price
   case general_depreciation_percentage
   case general_total_weight
   case general_after_depreciation
   case general_price_per_kg
   case general_total_amount
   case general_weighing_list
   case general_no_data
   case general_update
   case general_old_value
   case general_export_volume
   case general_depreciation
   case general_total_export_amount
   case general_defective_volume
   case general_total_defective_amount
   case general_bulk_volume
   case general_total_bulk_amount
   case general_total_depreciation
   case general_average_price
   case general_enter_weight
   case actions_add
   case general_enter_info
   case general_crateID
   case general_vibrate_5_crates
   case general_auto_add
   case general_two_digits
   case general_three_digits
   case general_total_crate
   case actions_start

}

extension MKText {
    var text: String {
        return rawValue
    }

    var localized: String {
        let language = Locale.preferredLanguages.first ?? "en"
        if let path = Bundle.main.path(forResource: language, ofType: "lproj") {
            let bundle = Bundle(path: path)
            if let string = bundle?.localizedString(forKey: text, value: nil, table: nil) {
                return string.capFirstLetter()
            }
        }
        
        return NSLocalizedString(text, comment: "").capFirstLetter()
    }
    
    func format(_ arguments: CVarArg...) -> String {
        let value = NSLocalizedString(text, comment: "")
        return String(format: value, arguments: arguments)
    }
    
    static func updateLocalize(_ lang: String) {
        UserDefaults.standard.setValue([lang], forKey: "AppleLanguages")
    }
}

extension String {
    func capFirstLetter() -> String {
        return self.isEmpty ? self : prefix(1).capitalized + dropFirst()
    }

    mutating func capitalizeFirstLetter() {
        self = self.capitalizingFirstLetter()
    }
}